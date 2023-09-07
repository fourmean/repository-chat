# Импорт FastAPI и других необходимых модулей
from fastapi import FastAPI
from repository import UserRepository, ChatRepository
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создание FastAPI приложения
app = FastAPI()

# URL и подключение к базе данных
DATABASE_URL = "postgresql://postgres:root@localhost/repository_chat"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание таблиц в базе данных, если их нет
Base.metadata.create_all(bind=engine)

# Инициализация сессии базы данных
db_session = SessionLocal()

# Создание репозиториев для работы с пользователями и чатами
user_repo = UserRepository(db_session)
chat_repo = ChatRepository(db_session)


# Корневой маршрут для проверки работоспособности
@app.get("/")
async def read_root():
    return {"message": "Hello, this is a test task"}


# Маршрут для получения всех пользователей
@app.get("/users")
def get_all_users():
    users = user_repo.get_all_users()
    return [{"id": user.id, "username": user.username, "photo_url": user.photo_url} for user in users]


# Маршрут для получения пользователя по ID
@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    user = user_repo.get_user_by_id(user_id)
    if user:
        return {"id": user.id, "username": user.username}
    else:
        return {"message": "User not found"}


# Маршрут для получения пользователя по имени пользователя
@app.get("/user/by_username")
def get_user_by_username(username: str):
    user = user_repo.get_user_by_username(username)
    if user:
        return {"id": user.id, "username": user.username, "photo_url": user.photo_url}
    else:
        return {"message": "User not found"}


# Маршрут для получения чатов пользователя
@app.get("/user/{user_id}/chats")
def get_user_chats(user_id: int):
    user_chats = user_repo.get_user_chats(user_id)
    return user_chats


# Маршрут для получения количества сообщений в чате
@app.get("/chat/messages/count/{chat_id}")
def get_message_count_in_chat(chat_id: int):
    message_count = chat_repo.get_message_count_in_chat(chat_id)
    return {"chat_id": chat_id, "message_count": message_count}


# Маршрут для получения сообщений между отправителем и получателем
@app.get("/chat/messages")
def get_messages(sender_id: int, receiver_id: int):
    messages = chat_repo.get_messages(sender_id, receiver_id)
    return messages


# Маршрут для получения количества чатов по статусу
@app.get("/chat/count")
def get_chat_count_by_status(status: int):
    chat_count = chat_repo.get_chat_count_by_status(status)
    return {"status": status, "chat_count": chat_count}


# Запуск FastAPI приложения
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
