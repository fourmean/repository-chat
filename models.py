from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    photo_url = Column(String, nullable=False)


class Chat(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    status = Column(SmallInteger, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class UserChat(Base):
    __tablename__ = 'user_chats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey('chats.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    chat = relationship('Chat')
    user = relationship('User')


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(String, nullable=False)
    time_delivered = Column(DateTime, nullable=False)
    time_seen = Column(DateTime)
    is_delivered = Column(Boolean, default=False, nullable=False)
    chat_id = Column(Integer, ForeignKey('chats.id'), nullable=False)
