from spider.tasks import tg_names_to_analyze

def spider_name(tgname, start0, start1):
    task = tg_names_to_analyze.delay(tgname, start0, start1)
    print(task.get())
