# -*- coding: utf-8 -*-
import scrapy
import redis_spider

class LinkSpider(redis_spider.RedisSpider):
    name = "link"
    allowed_domains = ["www.baidu.com"]


    def parse(self, response):
        print response

