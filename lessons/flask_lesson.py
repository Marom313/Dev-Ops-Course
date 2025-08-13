# Project Flask-Discord integration
import sqlite3
from discordwebhook import Discord
from datetime import datetime, timedelta
import requests as req

from flask import Flask, render_template, request, jsonify

# initialize flask app
app = Flask(__name__)

# setup a SQL DB
conn = sqlite3.connect('messages.db')
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS messages
               (
                   id
                   INTEGER
                   PRIMARY
                   KEY
                   AUTOINCREMENT,
                   content
                   TEXT
                   NOT
                   NULL,
                   timestamp
                   DATETIME
                   NOT
                   NULL
                   DEFAULT
                   CURRENT_TIMESTAMP
               );
               """)
conn.commit()

# discord_webhook_URL
discord_webhook_url = 'https://discord.com/api/webhooks/1404765562982109194/7cuoe5Q-OUZaiPzgdWxuVqOajrsuQSsNlgZgP_WctfpRANk_4mPd3zIp_VIZkICzC7Bm'


# Endpoint 3: Message retrieval
@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        cutoff_time = datetime.utcnow() - timedelta(minutes=30)
        cursor.execute('SELECT content,timestamp FROM messages WHERE timestamp >= ?', (cutoff_time,))
        messages = cursor.fetchall()
        return jsonify({"status": "success", "messages": messages})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


# Endpoint 2: Gets a msg and url and integrate it with discord.
def send_to_discord(message, webhook_url):
    payload = {"content": message}
    response = req.post(webhook_url, json=payload)
    response.raise_for_status()


# Endpoint 1: Recive text from user using 'POST'
@app.route('/input_text', methods=['POST'])
def input_text():
    try:
        data = request.get_json()
        text = data['text']
        # Send text to Discord server
        send_to_discord(text)

        # Save text to DB SQLite
        save_to_database(text)

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


# Additional endpoint - Serving HTML page
@app.route('/')
def index():
    return render_template('index.html')


# Run the Flasp App
if __name__ == '__main__':
    app.run(debug=True)
