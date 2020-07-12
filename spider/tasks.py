from celery import Celery
from telethon import TelegramClient
from sqlalchemy.orm import sessionmaker

from .settings import API_ID, API_HASH, engine
from .channel_info import get_channel_info, update_channel_info
from .models import db


app = Celery('tasks', backend='amqp', broker='pyamqp://guest@localhost:5672//')

def start_spider_client():
    client_tg = TelegramClient('socpulce_tg', API_ID, API_HASH)
    client_tg.start()
    return client_tg

def start_spider_session():
    db.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session_db = DBSession()
    return session_db

globalStartClient = start_spider_client()
globalStartSession = start_spider_session()

@app.task(name="tg_names_to_analyze")
def tg_names_to_analyze(tg_name):
    # result_info_channel = get_channel_info(globalStartClient, tg_name)
    # update_channel_info(result_info_channel, globalStartSession)
    return tg_name

# task = tg_names_to_analyze.delay("bitkogan")
