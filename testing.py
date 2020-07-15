from spider.tasks import app

sig = app.signature('tg_names_to_analyze')
res = sig.delay("bitkogan")
