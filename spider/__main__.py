from telethon import TelegramClient, sync

from .settings import API_ID, API_HASH
from .channel_info import update_channel_info
from .model import db

def start_spider():
    # app.config.from_pyfile("settings.py")
    # db.init_app(app)

    client = TelegramClient('socpulce_tg', API_ID, API_HASH)
    client.start()

    update_channel_info(client, "pythonjuniorjob")

    return app