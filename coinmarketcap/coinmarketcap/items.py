# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CurrencyItem(scrapy.Item):
    coin_name = scrapy.Field()
    exchange_name = scrapy.Field()
    pair = scrapy.Field()
    volume_24h = scrapy.Field()
    price = scrapy.Field()
    volume_pc = scrapy.Field()
    updated = scrapy.Field()
