from spider.tasks import tg_names_to_analyze

def spider_name():
    task = tg_names_to_analyze.delay("bitkogan")
    print(task.get())
