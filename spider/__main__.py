from telethon import TelegramClient, sync
from flask import Flask

from .settings import API_ID, API_HASH
from .channel_info import get_channel_info
from .model import db

def start_spider():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    db.init_app(app)

    client = TelegramClient('socpulce_tg', API_ID, API_HASH)
    client.start()

    # Выводим собранную базовую информацию по каналу
    print(get_channel_info(client, "pythonjuniorjob"))

    return app