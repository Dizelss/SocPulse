from sqlalchemy import create_engine
from spider.models import db


engine = create_engine("sqlite:///socpulse_tg.db")
db.metadata.create_all(engine)
