# Repository Chat API

Добро пожаловать в **Repository Chat API**! Это RESTful API для управления чатами и сообщениями между пользователями. С
помощью этого API вы можете получать информацию о пользователях, их чатах и сообщениях.

## Установка и запуск

Чтобы развернуть и запустить проект локально, выполните следующие шаги:

1. **Клонируйте репозиторий** на свой локальный компьютер:

    ```bash
    git clone https://github.com/fourmean/repository-chat.git
    ```

3. **Создайте и активируйте виртуальное окружение** (рекомендуется):

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

4. **Установите зависимости**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Примените миграции** для базы данных:

    ```bash
    alembic upgrade head
    ```

6. **Запустите сервер FastAPI**:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

После выполнения этих шагов, API будет доступно по адресу [http://localhost:8000](http://localhost:8000).

### Docker

Если вы предпочитаете использовать Docker, выполните следующие шаги:

1. **Соберите Docker образ**:

    ```bash
    docker-compose build
    ```

2. **Запустите Docker контейнеры**:

    ```bash
    docker-compose up
    ```

После выполнения этих шагов, API будет доступно по адресу [http://localhost:8000](http://localhost:8000).

## Использование

Для работы с API используйте следующие эндпоинты:

- **Получить список всех пользователей**:

    ```http
    GET /users
    ```

- **Получить пользователя по ID**:

    ```http
    GET /user/{user_id}
    ```

- **Получить пользователя по имени пользователя**:

    ```http
    GET /user/by_username?username={username}
    ```

- **Получить чаты пользователя**:

    ```http
    GET /user/{user_id}/chats
    ```

- **Получить количество сообщений в чате**:

    ```http
    GET /chat/messages/count/{chat_id}
    ```

- **Получить сообщения между отправителем и получателем**:

    ```http
    GET /chat/messages?sender_id={sender_id}&receiver_id={receiver_id}
    ```

- **Получить количество чатов по статусу**:

    ```http
    GET /chat/count?status={status}
    ```

## Технологии

- Python 3.10
- SQLAlchemy
- FastAPI
- Docker

## Автор

**Фомин Роман Александрович**
