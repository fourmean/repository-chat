from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Chat, UserChat, Message
from datetime import datetime

# Устанавливаем соединение с базой данных PostgreSQL
DATABASE_URL = "postgresql://postgres:root@localhost/repository_chat"
engine = create_engine(DATABASE_URL)

# Создаем объект сессии для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def main():
    # Создаем сессию для выполнения операций с базой данных
    session = SessionLocal()

    # Создаем 5 пользователей
    for user_id in range(1, 6):
        user = User(
            id=user_id,
            username=f"user{user_id}",
            photo_url=f"photo{user_id}.jpg",
        )
        session.add(user)

    # Создаем чаты между пользователями (каждый с каждым)
    chat_counter = 641  # Начальное значение идентификатора чата
    for user1_id in range(1, 6):
        for user2_id in range(1, 6):
            if user1_id != user2_id:
                chat_name = f"Chat_{user1_id}_to_{user2_id}"
                chat = Chat(
                    id=chat_counter,  # Устанавливаем желаемый идентификатор чата
                    name=chat_name,
                    status=0,  # Устанавливаем статус по вашим правилам
                    updated_at=datetime.now(),
                )
                session.add(chat)
                chat_counter += 1

    # Фиксируем изменения в базе данных
    session.commit()

    # Создаем сообщения между пользователями
    for user_id in range(1, 6):
        for chat_id in range(641, 661):  # Идентификаторы чатов от 641 до 660
            # Создаем 5 сообщений в каждом чате
            for message_id in range(1, 6):
                sender_id = user_id
                receiver_id = user_id % 5 + 1  # Циклическая отправка сообщений

                message = Message(
                    sender_id=sender_id,
                    receiver_id=receiver_id,
                    text=f"Message {message_id}",
                    time_delivered=datetime.now(),
                    is_delivered=True,  # Устанавливаем статус по вашим правилам
                    chat_id=chat_id,
                )
                session.add(message)

                # Создаем связи UserChat
                user_chat1 = UserChat(chat_id=chat_id, user_id=sender_id)
                user_chat2 = UserChat(chat_id=chat_id, user_id=receiver_id)

                session.add(user_chat1)
                session.add(user_chat2)

    # Фиксируем изменения в базе данных
    session.commit()

    # Закрываем сессию после использования
    session.close()


if __name__ == "__main__":
    main()
