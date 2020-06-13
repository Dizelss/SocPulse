from telethon import TelegramClient, sync
from settings import API_ID, API_HASH
from telethon import functions, types


# Сделать функцию получения базовой информации про канал: название, число подписчиков.
def get_channel_info(channel_username):
    try:
        result = client(functions.channels.GetFullChannelRequest(channel=channel_username))
        # просмотр полученных данных в удобном виде
        # print(result.stringify())
        channel_id = result.full_chat.id
        subscribers_count = result.full_chat.participants_count
        return channel_id, subscribers_count
    except ValueError:
        print("Ошибка")
        if NameError:
            print("Неверно указано наименование канала")

client = TelegramClient('socpulce_tg', API_ID, API_HASH)
client.start()
get_channel_info("pythonjuniorjob")