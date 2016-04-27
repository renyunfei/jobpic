# -*- coding: utf-8 -*-

import logging

from scrapy.exceptions import NotConfigured
from scrapy.exceptions import IgnoreRequest

class MyTestMiddleware(object):

        self.data = data

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getBool('DOWNLOADER_MT'):
            raise NotConfigured
        cls(crawler.data)

    def process_request(self, request, spider):
        if 'kd' in request.meta:
            raise IgnoreRequest

    #def process_exception(self, request, exception, spider):
    #    pass
