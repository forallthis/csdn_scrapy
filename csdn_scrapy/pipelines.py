# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from csdn_scrapy.items import CsdnScrapyItem, CsdnDetailImageItem

class CsdnScrapyImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if isinstance(item, CsdnScrapyItem):
            yield scrapy.Request(item['from_ico'])
        elif isinstance(item, CsdnDetailImageItem):
            yield scrapy.Request(item['src'])
        else:
            pass


class CsdnScrapyPipeline(object):
    def __init__(self):
        self.fc = open('csdn_detail.txt', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.fc.write(content)
        return item

    def close_spider(self, spider):
        self.fc.close()