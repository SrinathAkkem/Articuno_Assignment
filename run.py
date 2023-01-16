from app import app
from Model import MessageModel, LikeModel
from sqlalchemy import create_engine
from config import Config

if __name__ == '__main__':
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    message_model = MessageModel(engine)
    like_model = LikeModel(engine)
    app.run(debug=True)