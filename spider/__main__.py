from telethon import TelegramClient, sync

from .settings import API_ID, API_HASH
from .channel_info import update_channel_info

def start_spider():
    client = TelegramClient('socpulce_tg', API_ID, API_HASH)
    client.start()

    update_channel_info(client, "pythonjuniorjob")
