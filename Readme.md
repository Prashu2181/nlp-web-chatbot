# NLP Web Chatbot

A web-based NLP chatbot built using Flask that performs sentiment analysis and provides intelligent responses.  
The application supports multilingual input, voice interaction, and includes a chat analytics dashboard.

---

## 🚀 Features

- Sentiment analysis (Positive / Negative / Neutral)
- Multilingual support (English, Telugu, Hindi)
- Voice input using browser Speech API
- Clean chat UI with message history
- Chat analytics dashboard (sentiment counts & visualization)
- Modular and extensible backend architecture
- AI integration ready (future enhancement)

---

## 🛠️ Tech Stack

Backend:
- Python
- Flask
- Flask-CORS
- NLTK
- TextBlob

Frontend:
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

web-chatbot-project/
├── backend/
│   ├── app.py
│   ├── logger.py
│   ├── templates/
│   │   ├── index.html
│   │   └── analytics.html
│   └── static/
│       ├── style.css
│       └── script.js
├── logs/
│   └── chat_logs.json
├── venv/
├── .gitignore
└── README.md

---

## ⚙️ How to Run the Project Locally

### Step 1: Clone the Repository

git clone https://github.com/YOUR_USERNAME/nlp-web-chatbot.git  
cd nlp-web-chatbot

---

### Step 2: Create and Activate Virtual Environment (Windows)

python -m venv venv  
venv\Scripts\activate

---

### Step 3: Install Dependencies

pip install -r requirements.txt

If requirements.txt is not available, install manually:

pip install flask flask-cors nltk textblob googletrans==4.0.0-rc1

---

### Step 4: Download Required NLTK Data

python

import nltk  
nltk.download('vader_lexicon')  
exit()

---

### Step 5: Run the Flask Application

python -m backend.app

You should see:

Running on http://127.0.0.1:5000

---

### Step 6: Open the Application in Browser

Chat UI:  
http://127.0.0.1:5000

Analytics Dashboard:  
http://127.0.0.1:5000/analytics

---

## 🎤 Voice Input

- Works best in Google Chrome
- Click the microphone icon and allow microphone access
- Spoken text will be converted to chat input

---

## 🌐 Multilingual Support

- Language selection available in UI
- Supported languages:
  - English
  - Telugu
  - Hindi

---

## 📊 Chat Analytics

- All chat messages are logged in JSON format
- Analytics page displays:
  - Total message count
  - Sentiment-wise distribution
  - Bar chart visualization

---

## 🔮 Future Enhancements

- Integration with Generative AI models (Gemini / OpenAI)
- Context-aware conversation handling
- User authentication
- Database-backed chat storage
- Advanced real-time analytics

---

## ⚠️ Notes

- API keys should not be committed to GitHub
- Virtual environment (venv) is ignored using .gitignore
- AI-based question answering is designed as a future enhancement

---

## 👨‍💻 Author

Prasanna  
Data Analytics & Software Development Enthusiast

---

## 📜 License

This project is developed for educational purposes.
