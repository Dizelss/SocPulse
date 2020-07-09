from telethon import TelegramClient, sync
from sqlalchemy.orm import sessionmaker

from .settings import API_ID, API_HASH, engine
from .channel_info import get_channel_info, update_channel_info
from .channel_posts import get_all_messages
from spider.models import db
from spider.producer_tasks import spider_name


def start_spider():
    client = TelegramClient('socpulce_tg', API_ID, API_HASH)
    client.start()

    db.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return client, session


start = start_spider()
spider_name("bitkogan", start[0], start[1])
print("Завершено")

# result_info_channel = get_channel_info(start[0], "zloyinvestor")
# update_channel_info(result_info_channel, start[1])
# get_all_messages(start[0], "pythonist_ru")
