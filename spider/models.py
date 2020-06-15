from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base


db =  declarative_base()

class TgChannels(db):
    __tablename__ = "TgChannels"
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, unique=True, nullable=False)
    channel_name = Column(String(250), nullable=False)
    subscribers_count = Column(Integer, nullable=False)
    category = Column(String(250), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __str__(self):
        return f"{self.channel_name}: подписчиков {self.subscribers_count}, категория {self.category}"
