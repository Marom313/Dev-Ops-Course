#  this is the Database file


import sqlite3
from datetime import datetime, timedelta
import os

# DB_PATH = os.path.join(os.path.dirname(__file__), "messages.db")
DB_PATH = "messages.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS messages
                (
                    id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    content    TEXT     NOT NULL,
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """)
    conn.commit()
    conn.close()


def save_to_db(msg: str) -> int:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
                INSERT INTO messages (content)
                VALUES (?)""", (msg,))
    last_id = cur.lastrowid
    conn.commit()
    conn.close()
    return last_id


def get_recent_messages(minutes: int = 30):
    cutoff = datetime.utcnow() - timedelta(minutes=minutes)
    cutoff_str = cutoff.strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""
                SELECT id, content, created_at
                FROM messages
                WHERE created_at >= ?
                ORDER BY created_at DESC
                """, (cutoff_str,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows
