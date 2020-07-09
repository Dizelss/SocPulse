from celery import Celery

from spider.channel_info import get_channel_info, update_channel_info


app = Celery('tasks', backend='amqp', broker='pyamqp://guest@localhost:5672//')


@app.task(name="tg_names_to_analyze")
def tg_names_to_analyze(tg_name):
    result_info_channel = get_channel_info(start[0], tg_name)
    update_channel_info(result_info_channel, start[1])
    return f"задача выполнена, {result_info_channel}"
