# -*- coding: utf-8 -*-
import redis_spider


class Link2Spider(redis_spider.RedisSpider):
    name = "link2"
    allowed_domains = ["www.baidu.com"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

    def parse(self, response):
        print response

