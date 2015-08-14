# -*- coding: utf-8 -*-
import scrapy
import redis_spider
from scrapy.exceptions import CloseSpider
class LinkSpider(redis_spider.RedisSpider):
    name = "link"
    allowed_domains = ["www.baidu.com"]

    def parse(self, response):
        if self.paused:
            print 'close spider link'
            raise CloseSpider(reason='API usage exceeded')
        print response

