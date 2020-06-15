# Сделать функцию получения всех постов канала. get_all_messages(channel_id)
def get_all_messages(client, channel_username):
    result = client.get_entity(channel_username)
    messages = client.get_messages(result, limit=3)
    return messages
