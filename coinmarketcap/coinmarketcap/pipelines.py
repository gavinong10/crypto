# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import boto3
import datetime
from pytz import timezone
import re



class CoinExchangePipeline(object):
    def process_item(self, item, spider):
        # Query for the URL and obtain a list of the versions.abs
        # Compare the newest version's HTML to the current one. 
        # If different or non-existent, then put/update the entry with a new version entry.
        # A version entry has fields: date_discovered, listing_html, listing_name, mail, version_no

        # Mail is used to track which mailing lists have already sent emails for the discovered listing.
        
        #### START MONGODB ####
        # TODO: Incorporate $currentDate	
        
        pass