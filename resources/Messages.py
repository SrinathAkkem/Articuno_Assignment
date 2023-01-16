import datetime
from flask import request, jsonify
from sqlalchemy.orm import sessionmaker

from Model import MessageModel

class Message():
    def __init__(self, conn):
        self.conn = conn

    def post_message(self, data):
        text = data['text']
        user = data['user']
        timestamp = datetime.now()

        message = MessageModel(text=text, user=user, timestamp=timestamp)

        Session = sessionmaker(bind=self.conn)
        session = Session()

        session.add(message)
        session.commit()

        return jsonify(success=True)

    def get_messages(self):
        Session = sessionmaker(bind=self.conn)
        session = Session()

        messages = session.query(MessageModel).order_by(MessageModel.timestamp.desc()).all()

        return jsonify([m.serialize for m in messages])