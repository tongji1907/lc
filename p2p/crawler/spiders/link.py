# -*- coding: utf-8 -*-
import scrapy


class LinkSpider(scrapy.Spider):
    name = "link"
    allowed_domains = ["www.baidu.com"]
    start_urls = (
        'http://www.www.baidu.com/',
    )

    def parse(self, response):
        print response
