from spider.model import db
from spider.__main__ import start_spider

db.create_all(app=start_spider())