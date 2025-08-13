#  this is the App file
from flask import Flask, jsonify, request, render_template
from db import init_db, get_recent_messages, save_to_db
# import requests as R
from discord_service import send_to_discord

app = Flask(__name__)
init_db()


@app.get("/get_messages")
def get_messages():
    try:
        messages = get_recent_messages()
        return jsonify({"status": "success", "messages": messages})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.post("/input_text")
def input_text():
    try:
        data = request.get_json(silent=True) or {}
        text = (data.get("text") or "").strip()
        if not text:
            return jsonify({"status": "error", "message": "text is required"}), 400

        send_to_discord(text)

        save_to_db(text)

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.get("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    print(">>>>> Running app from: ", __file__)
    app.run(debug=True)
