# -*- coding: utf-8 -*-

import logging

from scrapy.exceptions import NotConfigured
from scrapy.exceptions import IgnoreRequest

class MyTestMiddleware(object):

    #def __init__(self, crawler):
    #    if not crawler.settings.get('DOWNLOADER_MT'):
    #        raise NotConfigured

    #@classmethod
    #def from_crawler(cls, crawler):
    #    cls(crawler)

    def process_request(self, request, spider):
        if 'kd' in request.meta:
            #raise IgnoreRequest
            request.meta['kd'] = 'renyunfei'

        return

    #def process_exception(self, request, exception, spider):
    #    pass
