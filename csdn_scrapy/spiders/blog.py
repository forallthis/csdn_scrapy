# -*- coding: utf-8 -*-
import scrapy
import json
from csdn_scrapy.items import CsdnScrapyItem, CsdnDetailImageItem

class BlogSpider(scrapy.Spider):
    name = "csdnblog"
    allowed_domains = ["blog.csdn.net"]
    offerset = 0
    base_url = 'http://blog.csdn.net/api/articles?type=more&category=news&shown_offset='
    #start_urls = ['http://blog.csdn.net/nav/news']
    start_urls = [
        base_url + str(offerset)
    ]

    def parse(self, response):
        #网页中xpath提取
        # article_list = response.xpath('//div[@class="list_con"]')

        # for article in article_list:
        #     item = CsdnScrapyItem()
        #     item['title'] = article.xpath('./h2/a/text()')[0].extract().strip()
        #     item['from_ico'] = article.xpath('.//dl/dt/a/img/@src')[0].extract()
        #     item['from_site'] = article.xpath('./dl/dd[1]/a/text()')[0].extract().strip()
        #     item['time'] = article.xpath('./dl/dd[2]/text()')[0].extract().strip()
        #     item['read_num'] = article.xpath('./dl/dd[@class="read_num"]/text()').extract()[1].strip()
        #     print(item)

        #json提取

        article_list = json.loads(response.body)['articles']
        if not article_list:
            return

        for article in article_list:
            item = CsdnScrapyItem()
            item['title'] = article['title']
            item['from_ico'] = 'http:' + article['avatar']
            item['from_site'] = article['nickname']
            item['time'] = article['created_at']
            item['read_num'] = article['views']
            request = scrapy.Request(article['url'], callback=self.parse_detail)
            request.meta['item'] = item
            yield request

        if self.offerset < (10 * 1):
            self.offerset += 10
            yield scrapy.Request(self.base_url + str(self.offerset), callback=self.parse)

    def parse_detail(self, response):
        content = response.xpath('//div[@id="article_content"]')[0].extract()
        detail_item = response.meta['item']
        detail_item['content'] = content
        yield detail_item
        img_list = response.xpath('//div[@id="article_content"]//img')
        for img in img_list:
            item = CsdnDetailImageItem()
            item['src'] = img.xpath('@src')[0].extract()
            yield item
