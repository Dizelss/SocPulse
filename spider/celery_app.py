from celery import Celery


app = Celery('tasks', backend='amqp', broker='pyamqp://guest@localhost:5672//')
