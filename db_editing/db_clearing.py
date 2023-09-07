from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Chat, UserChat, Message

DATABASE_URL = "postgresql://postgres:root@localhost/repository_chat"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = SessionLocal()

db_session.query(Message).delete()
db_session.query(UserChat).delete()
db_session.query(Chat).delete()
db_session.query(User).delete()


db_session.commit()
db_session.close()
