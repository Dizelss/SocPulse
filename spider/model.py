from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TgChannels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Integer, unique=True, nullable=False)
    channel_name = db.Column(db.String, nullable=False)
    subscribers_count = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DataTime, nullable=False)
    updated_at = db.Column(db.DataTime, nullable=False)

    def __repr__(self):
        return f"{self.channel_name}: подписчиков {self.subscribers_count}, категория {self.category}"
