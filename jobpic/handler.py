# -*- coding: utf-8 -*-

import json
import jieba
from celery import Celery

app = Celery('lagou', broker='redis://192.168.181.128/3')

@app.task(name='ithot.handler.handler')
def handler(item):

    item = json.loads(item)
    detail = item['kd']

    for dt in detail:
        kd = dt.encode('UTF-8')
