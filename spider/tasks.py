from celery import Celery


app = Celery('tasks', backend='amqp', broker='pyamqp://guest@localhost:5672//')

@app.task(name="tg_names_to_analyze")
def tg_names_to_analyze(tg_name):
    tg_name_result = tg_name
    return tg_name_result
