# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IthotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    local = scrapy.Field()
    stage = scrapy.Field()
    time = scrapy.Field()
    cate = scrapy.Field()
    lang = scrapy.Field()
    skill = scrapy.Field()

    salary = scrapy.Field()
    years = scrapy.Field()
    local = scrapy.Field()
    edu = scrapy.Field()
    detail = scrapy.Field()
    pd = scrapy.Field()
    kd = scrapy.Field()
