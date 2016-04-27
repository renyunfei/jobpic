# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from urllib import urlencode, quote
from ithot.items import IthotItem
from scrapy.loader import ItemLoader

class ExampleSpider(scrapy.Spider):
    name = "hot"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com',
    )

    def parse(self, response):
        xp = '//*[@id="sidebar"]/div[1]/div/div/dl/dd/a/text()'

        for sel in response.xpath(xp).extract():
            item=IthotItem()
            kd = quote(sel.encode('utf-8'))

            city = '%E4%B8%8A%E6%B5%B7'
            data = {'first':'false', 'pn':1, 'kd':kd}

            #while True:
            i = 1
            data['pn'] = i

            url = 'http://www.lagou.com/jobs/positionAjax.json?city=' + city
            r = requests.post(url, data)
            #if not r.text:
            #    continue

            ret = json.loads(r.text.encode('utf-8'))

            result = ret['content']['result']
            for item in result:
                pd = item['positionId']

                job_url = 'http://www.lagou.com/jobs/' + str(pd) + '.html'
                yield scrapy.Request(url=job_url, meta = {'pd':pd, 'kd':kd},
                        callback=self.parse_detail, errback=self._err_process)

    def _err_process(self):
        print 'request error'

    def parse_detail(self, response):

        pd = response.meta['pd']
        kd = response.meta['kd']
        l = ItemLoader(item=IthotItem(), response=response)
        l.add_xpath('salary', '//*[@id="job_detail"]/dd[1]/p[1]/span[1]/text()')
        l.add_xpath('local', '//*[@id="job_detail"]/dd[1]/p[1]/span[2]/text()')

        l.add_xpath('years', '//*[@id="job_detail"]/dd[1]/p[1]/span[3]/text()')
        l.add_xpath('edu', '//*[@id="job_detail"]/dd[1]/p[1]/span[4]/text()')
        l.add_xpath('detail', '//*[@id="job_detail"]/dd[2]/p/text()')
        l.add_xpath('detail', '//*[@id="job_detail"]/dd[2]/p/span/text()')
        l.add_xpath('detail', '//*[@id="job_detail"]/dd[2]/ul/li/text()')
        l.add_xpath('detail', '//*[@id="job_detail"]/dd[2]/ul/li/p/text()')
        l.add_value('pd', pd)
        l.add_value('kd', kd)

        return l.load_item()
