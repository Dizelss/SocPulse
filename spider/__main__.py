from telethon import TelegramClient, sync
from settings import API_ID, API_HASH
from channel_info import get_channel_info

# Подключаемся
client = TelegramClient('socpulce_tg', API_ID, API_HASH)
client.start()

# Выводим собранную базовую информацию по каналу
print(get_channel_info(client, "pythonjuniorjob"))
