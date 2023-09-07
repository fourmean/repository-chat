import httpx

# URL вашего FastAPI приложения
api_url = "http://localhost:8000"

# Создаем HTTP-клиент
client = httpx.AsyncClient()


# Метод для извлечения всех пользователей
async def get_all_users():
    response = await client.get(f"{api_url}/users")
    return response.json()


# Метод для извлечения пользователя по ID
async def get_user_by_id(user_id):
    response = await client.get(f"{api_url}/user/{user_id}")
    return response.json()


# Метод для извлечения пользователя по имени пользователя (закомментирован, так как не используется в текущей версии)
# async def get_user_by_username(username):
#     response = await client.get(f"{api_url}/user/by_username", params={"username": username})
#     return response.json()

# Метод для извлечения чатов пользователя
async def get_user_chats(user_id):
    response = await client.get(f"{api_url}/user/{user_id}/chats")
    return response.json()


# Метод для извлечения количества сообщений в чате
async def get_message_count_in_chat(chat_id):
    response = await client.get(f"{api_url}/chat/messages/count/{chat_id}")
    return response.json()


# Метод для извлечения сообщений между отправителем и получателем
async def get_messages(sender_id, receiver_id):
    params = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
    }
    response = await client.get(f"{api_url}/chat/messages", params=params)
    return response.json()


# Метод для извлечения количества чатов по статусу
async def get_chat_count_by_status(status):
    response = await client.get(f"{api_url}/chat/count", params={"status": status})
    return response.json()


# Основная функция для взаимодействия с командной строкой
async def main():
    while True:
        print("Выберите действие:")
        print("1. Извлечь всех пользователей")
        print("2. Извлечь пользователя по ID")
        # print("3. Извлечь пользователя по имени")
        print("3. Извлечь чаты пользователя")
        print("4. Извлечь количество сообщений в чате")
        print("5. Извлечь сообщения")
        print("6. Извлечь количество чатов по статусу")
        print("7. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            users = await get_all_users()
            print("All Users:", users)
        elif choice == "2":
            user_id = int(input("Введите ID пользователя: "))
            user = await get_user_by_id(user_id)
            print("User by ID:", user)
            # elif choice == "3":
            '''username = input("Введите имя пользователя: ")
            user_by_username = await get_user_by_username(username)
            print("User by Username:", user_by_username)'''
        elif choice == "3":
            user_id = int(input("Введите ID пользователя: "))
            user_chats = await get_user_chats(user_id)
            print("User Chats:", user_chats)
        elif choice == "4":
            chat_id = int(input("Введите ID чата: "))
            message_count = await get_message_count_in_chat(chat_id)
            print("Message Count in Chat:", message_count)
        elif choice == "5":
            sender_id = int(input("Введите ID отправителя: "))
            receiver_id = int(input("Введите ID получателя: "))
            messages = await get_messages(sender_id, receiver_id)
            print("Messages:", messages)
        elif choice == "6":
            status = int(input("Введите статус чата: "))
            chat_count = await get_chat_count_by_status(status)
            print("Chat Count by Status:", chat_count)
        elif choice == "7":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

    await client.aclose()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
