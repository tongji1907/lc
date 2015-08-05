# -*- coding: utf-8 -*-
import scrapy


class Link2Spider(scrapy.Spider):
    name = "link2"
    allowed_domains = ["www.baidu.com"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

    def parse(self, response):
        print response

