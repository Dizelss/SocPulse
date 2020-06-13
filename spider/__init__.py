from telethon import TelegramClient, sync

from .settings import API_ID, API_HASH
from .channel_info import get_channel_info
# from .model import db




# app = Flask(__name__)
# app.config.from_pyfile("settings.py")
# db.init_app(app)

if __name__ == "__main__":
    client = TelegramClient('socpulce_tg', API_ID, API_HASH)
    client.start()
    # Выводим собранную базовую информацию по каналу
    print(get_channel_info(client, "pythonjuniorjob"))