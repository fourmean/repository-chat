from sqlalchemy.orm import Session
from models import User, Chat, UserChat, Message


# Репозиторий пользователей
class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    # Получить список всех пользователей
    def get_all_users(self):
        return self.db_session.query(User).all()

    # Получить пользователя по ID
    def get_user_by_id(self, user_id):
        return self.db_session.query(User).filter(User.id == user_id).first()

    # Получить пользователя по имени пользователя (username)
    def get_user_by_username(self, username):
        return self.db_session.query(User).filter(User.username == username).first()

    # Получить чаты пользователя по user_id, с возможностью фильтрации по статусу
    def get_user_chats(self, user_id, status=None):
        # Создаем запрос, объединяя таблицы Chat, UserChat и User, и фильтруя результаты
        query = (
            self.db_session.query(Chat, User)
            .join(UserChat, UserChat.chat_id == Chat.id)
            .join(User, UserChat.user_id == User.id)
            .filter(User.id == user_id)
            .filter(Chat.name.ilike(f"%_to_{user_id}"))
        )

        # Проверяем наличие фильтра по статусу
        if status is not None:
            query = query.filter(Chat.status == status)

        chat_data = []
        # Обрабатываем результаты запроса и формируем информацию о чатах
        for chat, other_user in query.all():
            chat_data.append({
                "chat_id": chat.id,
                "chat_name": chat.name,
                "other_user": other_user.username,
            })

        return chat_data


# Репозиторий чатов
class ChatRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    # Получить сообщения между отправителем (sender_id) и получателем (receiver_id)
    def get_messages(self, sender_id, receiver_id):
        return self.db_session.query(Message).filter(
            (Message.sender_id == sender_id) | (Message.sender_id == receiver_id),
            (Message.receiver_id == sender_id) | (Message.receiver_id == receiver_id),
        ).all()

    # Получить количество сообщений в чате по chat_id
    def get_message_count_in_chat(self, chat_id):
        return self.db_session.query(Message).filter(Message.chat_id == chat_id).count()

    # Получить количество чатов с заданным статусом
    def get_chat_count_by_status(self, status):
        return self.db_session.query(Chat).filter(Chat.status == status).count()
