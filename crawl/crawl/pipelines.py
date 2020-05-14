# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class CrawlPipeline:

    def __init__(self):
        self.connection = pymongo.MongoClient("mongodb+srv://dbuser:12345@cluster0-cnvdh.gcp.mongodb.net/test?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
        db = self.connection['quotesdata']
        self.collection = db['quotes']


    def process_item(self, item, spider):
        # pass the item containing data 
        self.collection.insert(dict(item))
        return item
