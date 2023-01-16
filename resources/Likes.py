import datetime
from flask import request, jsonify
from sqlalchemy.orm import sessionmaker

from Model import LikeModel

class Like():
    def __init__(self, conn):
        self.conn = conn

    def like_message(self, message_id, data):
        user = data['user']
        timestamp = datetime.now()

        like = LikeModel(message_id=message_id, user=user, timestamp=timestamp)

        Session = sessionmaker(bind=self.conn)
        session = Session()

        session.add(like)
        session.commit()

        return jsonify(success=True)

    def get_message_likes(self, message_id):
        Session = sessionmaker(bind=self.conn)
        session = Session()

        likes = session.query(LikeModel).filter_by(message_id=message_id).all()

        return jsonify([l.serialize for l in likes])

    def get_likes_count(self, message_id):
        Session = sessionmaker(bind=self.conn)
        session = Session()

        count = session.query(LikeModel).filter_by(message_id=message_id).count()

        return jsonify(count=count)