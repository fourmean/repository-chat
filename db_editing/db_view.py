from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Chat, UserChat, Message

# Устанавливаем соединение с базой данных PostgreSQL
DATABASE_URL = "postgresql://postgres:root@localhost/repository_chat"
engine = create_engine(DATABASE_URL)

# Создаем объект сессии для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = SessionLocal()

# Выбираем всех пользователей из таблицы "users"
users = db_session.query(User).all()

# Выбираем все чаты из таблицы "chats"
chats = db_session.query(Chat).all()

# Выбираем связи пользователей с чатами из таблицы "userchats"
userchats = db_session.query(UserChat).all()

# Выбираем все сообщения из таблицы "messages"
messages = db_session.query(Message).all()

# Выводим информацию о пользователях
print("Пользователи:")
for user in users:
    print(f"ID пользователя: {user.id}, Имя пользователя: {user.username}, URL фотографии: {user.photo_url}")

# Выводим информацию о чатах
print("\nЧаты:")
for chat in chats:
    print(f"ID чата: {chat.id}, Название чата: {chat.name}, Статус чата: {chat.status}, Обновлено: {chat.updated_at}")

# Выводим информацию о связях пользователей с чатами
print("\nСвязи пользователей и чатов:")
for userchat in userchats:
    print(f"ID связи: {userchat.id}, ID чата: {userchat.chat_id}, ID пользователя: {userchat.user_id}")

# Выводим информацию о сообщениях
print("\nСообщения:")
for message in messages:
    print(f"ID сообщения: {message.id}, ID отправителя: {message.sender_id}, ID получателя: {message.receiver_id}, "
          f"Текст: {message.text}, Доставлено: {message.time_delivered}, Прочитано: {message.time_seen}, "
          f"Доставлено успешно: {message.is_delivered}, ID чата: {message.chat_id}")

# Закрываем сессию после использования
db_session.close()
