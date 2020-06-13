from telethon import functions


def get_channel_info(client, channel_username):
    result = client(functions.channels.GetFullChannelRequest(channel=channel_username))
    channel_id = result.full_chat.id
    subscribers_count = result.full_chat.participants_count
    return channel_id, subscribers_count
