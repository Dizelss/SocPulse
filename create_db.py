from spider.models import db
from spider.settings import engine


db.metadata.create_all(engine)
