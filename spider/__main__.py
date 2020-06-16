from telethon import TelegramClient, sync
from sqlalchemy.orm import sessionmaker

from .settings import API_ID, API_HASH, engine
from .channel_info import get_channel_info, update_channel_info
from .channel_posts import get_all_messages
from spider.models import db


def start_spider():
    client = TelegramClient('socpulce_tg', API_ID, API_HASH)
    client.start()

    db.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    result_info_channel = get_channel_info(client, "FINASCOP")
    update_channel_info(result_info_channel, session)
    get_all_messages(client, "pythonist_ru")

start_spider()