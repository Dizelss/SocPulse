from telethon import functions
from datetime import datetime

from spider.models import TgChannels


def get_channel_info(client, channel_username):
    result = client(functions.channels.GetFullChannelRequest(channel=channel_username))
    channel_id = result.full_chat.id
    channel_name = channel_username
    subscribers_count = result.full_chat.participants_count
    category = ""
    created_at = datetime.now()
    updated_at = datetime.now()

    result_channel_info = {
        "channel_id": channel_id,
        "channel_name": channel_name,
        "subscribers_count": subscribers_count,
        "category": category,
        "created_at": created_at,
        "updated_at": updated_at
    }
    return result_channel_info

def update_channel_info(result_channel_info, session):
    try:
        edited_tg_channel = session.query(TgChannels).filter_by(channel_id=result_channel_info["channel_id"]).one()
        edited_tg_channel.category = "перезаписали категорию"
        edited_tg_channel.updated_at = datetime.now()
        session.add(edited_tg_channel)
    except:
        new_tg_channel = TgChannels(**result_channel_info)
        session.add(new_tg_channel)
    session.commit()
