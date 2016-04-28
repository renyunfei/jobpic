# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from requests import ConnectionError, HTTPError, Timeout
from urllib import urlencode, quote
from jobpic.items import IthotItem
from scrapy.loader import ItemLoader
from scrapy import log

class JobpicSpider(scrapy.Spider):
    name = "jobpic"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com',
    )

    cities = []

    def __init__(self, category=None, *args, **kwargs):
        for city in open('city.txt', 'r'):
            self.cities.append(city.strip())

    def parse(self, response):
        xp = '//*[@id="sidebar"]/div[1]/div/div/dl/dd/a/text()'

        for sel in response.xpath(xp).extract():
            item=IthotItem()
            kd = quote(sel.encode('utf-8'))

            for city in self.cities:
                for result in self._get_jobs(city, kd):
                    for item in result:
                        pd = item['positionId']
                        item['kd'] = kd

                        job_url = 'http://www.lagou.com/jobs/' + str(pd) + '.html'
                        yield scrapy.Request(url=job_url, meta = item,
                                callback=self.parse_detail, errback=self._err_process)


    def _get_jobs(self, city, kd):
        data = {'first':'false', 'pn':None, 'kd':kd}
        url = 'http://www.lagou.com/jobs/positionAjax.json?city=' + city
        page = 0
        totalpage = 1

        while page <= totalpage:
            page += 1
            data['pn'] = page

            #try:
            r = requests.post(url, data)
            #except ConnectionError, HTTPError, Timeout:
            #    log.msg('send request for get detail error', level=log.ERROR)

            result = json.loads(r.text.encode('utf-8'))['content']['result']
            if not totalpage:
                totalpage = json.loads(r.text.encode('utf-8'))['content']['totalPageCount']

            yield result

    def _err_process(self):
        log.msg('send request for get detail error', level=log.ERROR)

    def parse_detail(self, response):

        pd = response.meta['positionId']
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
