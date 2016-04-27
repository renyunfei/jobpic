# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from handler import handler
import json

class IthotPipeline(object):
    def process_item(self, item, spider):
        handler.delay(json.dumps(dict(item)))
        return item
