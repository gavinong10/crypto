import scrapy
from coinmarketcap.items import CurrencyItem
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import pandas as pd
import os
from functools import partial

dir_path = os.path.dirname(os.path.realpath(__file__))

class ExchangeListingsSpider(scrapy.Spider):
    name = "ExchangeListings"
    start_urls = ["https://coinmarketcap.com/all/views/all/"]

    series = pd.Series()
    rows = []

    def __init__(self):
        rows = []
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def parse_listing(self, response, coin_name=None):
        market_objs = response.xpath("//table[@id='markets-table']//tr")
        exchange_cols = []
        for market_obj in market_objs[1:]:
            tds = market_obj.xpath("./td")
            item = CurrencyItem(
                coin_name = coin_name,
                exchange_name = tds[1].xpath("./a/text()").extract_first(),
                pair = tds[2].xpath("./a/text()").extract_first(),
                volume_24h = tds[3].xpath("./span/text()").extract_first().strip(),
                price = tds[4].xpath("./span/text()").extract_first().strip(),
                volume_pc = tds[5].xpath("./text()").extract_first(),
                updated = tds[6].xpath("./text()").extract_first()
            )
            self.rows.append(dict(item))
    
    def parse(self, response):
        currency_link_objs = response.xpath("//a[@class='currency-name-container']")
        #currency_links = currency_link_objs.xpath("./@href").extract()
        #currency_names = currency_link_objs.xpath("./text()").extract()

        for link_obj in currency_link_objs:
            # Fetch the url
            url = link_obj.xpath("./@href").extract_first() + "#markets"
            coin_name = link_obj.xpath("./text()").extract_first()

            yield response.follow(url, callback=partial(self.parse_listing, coin_name=coin_name))

    def spider_closed(self, spider):
        print "#############\n\n#######"
        print spider.rows
        df = pd.DataFrame(spider.rows)
        df.to_csv(dir_path + "/../outputs/exchangespideroutput.csv")
