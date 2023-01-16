from datetime import datetime
from flask import request, jsonify

class MessageModel():
    def __init__(self, conn):
        self.conn = conn
        
    def post_message(self, data):
        text = data['text']
        user = data['user']
        timestamp = datetime.now()

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO messages (text, user, timestamp) VALUES (%s, %s, %s)", (text, user, timestamp))
        self.conn.commit()

        return jsonify(success=True)

    def get_messages(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM messages ORDER BY timestamp DESC")
        messages = cursor.fetchall()

        return jsonify(messages)


class LikeModel():
    def __init__(self, conn):
        self.conn = conn

    def like_message(self, message_id, data):
        user = data['user']
        timestamp = datetime.now()

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO likes (message_id, user, timestamp) VALUES (%s, %s, %s)", (message_id, user, timestamp))
        self.conn.commit()

        return jsonify(success=True)

    def get_message_likes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT message_id, COUNT(*) FROM likes GROUP BY message_id")
        likes = cursor.fetchall()

        return jsonify(likes)