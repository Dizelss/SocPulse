from spider.tasks import app

sig = app.signature('tg_names_to_analyze')
sig.delay("bitkogan")
