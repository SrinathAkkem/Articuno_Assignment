from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    user = Column(String)
    timestamp = Column(DateTime)

class Like(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    user = Column(String)
    timestamp = Column(DateTime)

def create_tables(engine):
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    engine = create_engine("postgresql://username:password@hostname/dbname")
    create_tables(engine)
