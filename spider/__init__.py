from telethon import TelegramClient, sync
from settings import API_ID, API_HASH
from telethon import functions, types

client = TelegramClient('socpulce_tg', API_ID, API_HASH)
client.start()

result = client(functions.channels.GetFullChannelRequest(
    channel='pythonjuniorjob'
))
# Выводим кол-во подписчиков паблика
print(result.stringify())
print(f"Количество подписчиков паблика: {result.full_chat.participants_count}")