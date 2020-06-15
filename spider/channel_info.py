from telethon import functions
from datetime import datetime

from .model import db, TgChannels


# Сделать функцию update_channel_info(channel_id),
# которая получает про канал всю нужную информацию
# и создает или обновляет соответствующую запись в БД
def update_channel_info(client, channel_username):
    result = client(functions.channels.GetFullChannelRequest(channel=channel_username))
    channel_id = result.full_chat.id
    channel_name = channel_username
    subscribers_count = result.full_chat.participants_count
    channel_category = "1"
    created_at = datetime.now()
    updated_at = datetime.now()

    channel_new = TgChannels(
        channel_id=channel_id,
        channel_name=channel_name,
        subscribers_count=subscribers_count,
        category=channel_category,
        created_at=created_at,
        updated_at=updated_at
    )
    print(channel_new)
    db.session.add(channel_new)
    db.session.commit()
