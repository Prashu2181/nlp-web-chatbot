from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from datetime import datetime
from googletrans import Translator
from backend.logger import log_chat, get_analytics
import google.generativeai as genai



app = Flask(__name__)
CORS(app)

sia = SentimentIntensityAnalyzer()
translator = Translator()


def analyze_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"


def correct_spelling(text):
    return str(TextBlob(text).correct())


def translate_to_english(text, lang):
    if lang == "en":
        return text
    return translator.translate(text, src=lang, dest="en").text


def translate_from_english(text, lang):
    if lang == "en":
        return text
    return translator.translate(text, src="en", dest=lang).text


def is_knowledge_question(text):
    question_words = ["what", "why", "how", "explain", "define"]
    text = text.lower().strip()
    return text.endswith("?") or any(text.startswith(q) for q in question_words)


responses = {
    "positive": [
        "That's great to hear!",
        "Awesome! Sounds positive.",
        "Nice, keep it up!"
    ],
    "neutral": [
        "I see. Tell me more.",
        "Okay, got it.",
        "Thanks for sharing."
    ],
    "negative": [
        "I'm sorry you're feeling this way.",
        "That sounds tough. I'm here to help.",
        "Hope things get better soon."
    ]
}


def get_ai_answer(question):
    try:
        genai.configure(api_key="YOUR_API_KEY")
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        print("Gemini error:", e)
        return "I'm having trouble answering that right now."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    original_message = data.get("message", "")
    language = data.get("language", "en")

    translated_input = translate_to_english(original_message, language)

    corrected_message = correct_spelling(translated_input)

    sentiment = analyze_sentiment(corrected_message)

    if is_knowledge_question(corrected_message):
        answer_en = get_ai_answer(corrected_message)
    else:
        answer_en = responses[sentiment][0]

    if sentiment == "negative":
        answer_en = "I understand this might be difficult. " + answer_en
    elif sentiment == "positive":
        answer_en = "Great question! " + answer_en

    final_reply = translate_from_english(answer_en, language)

    log_chat({
        "time": datetime.now().isoformat(),
        "message": original_message,
        "language": language,
        "sentiment": sentiment,
        "used_ai": is_knowledge_question(corrected_message)
    })

    return jsonify({
        "sentiment": sentiment,
        "bot_reply": final_reply
    })


@app.route("/analytics")
def analytics():
    data = get_analytics()
    return render_template("analytics.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
