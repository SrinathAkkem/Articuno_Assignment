from flask import Flask, request
from Model import MessageModel, LikeModel
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="hostname",
    user="username",
    password="password",
    dbname="dbname"
)

message_model = MessageModel(conn)
like_model = LikeModel(conn)

@app.route('/message', methods=['POST'])
def post_message():
    data = request.get_json()
    return message_model.post_message(data)

@app.route('/messages', methods=['GET'])
def get_messages():
    return message_model.get_messages()

@app.route('/like/<int:message_id>', methods=['POST'])
def like_message(message_id):
    data = request.get_json()
    return like_model.like_message(message_id, data)

@app.route('/messages/likes', methods=['GET'])
def get_message_likes():
    return like_model.get_message_likes()

if __name__ == '__main__':
    app.run(debug=True)
