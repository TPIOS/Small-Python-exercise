# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Item
from scrapy.exceptions import DropItem
from scrapy import signals
import datetime
import json

class CleanPipeline():
    def process_item(self, item, spider):
        if item['desc']:
            item['desc'] = item['desc'].strip().lower().replace('#$','')
            return item

class AgePipeline():
    def process_item(self, item, spider):
        if item['DOB']:
            item['Age'] = (datetime.datetime.strptime(item['DOB'], '%d-%m-%y').date()-datetime.datetime.strptime('currentdate', '%d-%m-%y').date()).days/365
            return item

class DuplicatesPipeline():
    def __init__(self):
        self.ids_seen = set()
    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item

class JsonWriterPipeline():
    def __init__(self):
        self.file = open('items.txt','wb')
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item