from flask import Flask, request, jsonify
from messages import Message
from likes import Like
from config import Config
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
message = Message(engine)
like = Like(engine)

@app.route('/message', methods=['POST'])
def post_message():
    data = request.get_json()
    return message.post_message(data)

@app.route('/messages', methods=['GET'])
def get_messages():
    return message.get_messages()

@app.route('/like/<int:message_id>', methods=['POST'])
def like_message(message_id):
    data = request.get_json()
    return like.like_message(message_id, data)

@app.route('/messages/<int:message_id>/likes', methods=['GET'])
def get_message_likes(message_id):
    return like.get_message_likes(message_id)

@app.route('/messages/<int:message_id>/likes/count', methods=['GET'])
def get_likes_count(message_id):
    return like.get_likes_count(message_id)
