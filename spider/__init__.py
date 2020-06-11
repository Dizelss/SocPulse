from telethon import TelegramClient, sync
from settings import API_ID, API_HASH


client = TelegramClient('socpulce_tg', API_ID, API_HASH)
client.start()

# выводим информацию о своем аккаунте
# print(client.get_me().stringify())

# отправляем сообщение другому аккаунту
# client.send_message('romanN005', 'Привет - это сообщение отправлено с помощью библиотеки Telethon')

# получаем информацию по каналу
# channel = client.get_entity("https://t.me/pythonjuniorjob")
# print(channel)