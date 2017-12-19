# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnScrapyItem(scrapy.Item):
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    title = scrapy.Field()
    from_ico = scrapy.Field()
    from_site = scrapy.Field()
    time = scrapy.Field()
    read_num = scrapy.Field()
    content = scrapy.Field()

class CsdnDetailImageItem(scrapy.Item):
    src = scrapy.Field()