import json
import os

LOG_FILE = "logs/chat_logs.json"

def log_chat(data):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(data)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


def get_analytics():
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    summary = {
        "positive": 0,
        "negative": 0,
        "neutral": 0,
        "total": len(logs)
    }

    for chat in logs:
        sentiment = chat.get("sentiment")
        if sentiment in summary:
            summary[sentiment] += 1

    return summary
