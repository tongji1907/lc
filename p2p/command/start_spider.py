#!/usr/bin/env python
from scrapy.crawler import CrawlerProcess
from threading import Thread
from scrapy.settings import Settings
from importlib import import_module
from scrapy.utils.project import get_project_settings
import sys
import os
import time
from scrapy.utils.misc import *
import logging
from sqlalchemy import *


settings = Settings()
settings_module_path = "settings"
if settings_module_path:
    settings.setmodule(settings_module_path, priority='project')

process = CrawlerProcess(settings)

def _start_crawler_thread():
    t = Thread(target=process.start,
                   kwargs={'stop_after_crawl': False})
    t.daemon = True
    t.start()



#s = import_module("..\\crawler\\settings.py")


linkSpider = 'p2p.crawler.spiders.link.LinkSpider'
linkSpider2 = 'p2p.crawler.spiders.link2.Link2Spider'

spider_cls = load_object(linkSpider)
spider2_cls = load_object(linkSpider2)
process.crawl(spider_cls)

#process.crawl(spider2_cls)

engines = []
crawlers = []
for crawler in process.crawlers:
    engines.append(crawler.engine)
    crawlers.append(crawler)


'''
crawler = process._create_crawler(spider_cls)
        # The Shell class needs a persistent engine in the crawler
crawler.engine = crawler._create_engine()
crawler.engine.start()
crawler.engine.open_spider(spider_cls)
crawler.engine.open_spider(spider2_cls)

'''
_start_crawler_thread()

while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break

    if not line:
        break

    if line == 'stop\n':
        print 'close link spider'
        #engines[0].close_spider(spider_cls)
        crawlers[0].stop()
    elif line=='start\n':
        print 'start link spider'
        #engines[0].open_spider(spider_cls)
        crawlers[0].crawl()
#process.crawl(spider_cls)

#process.crawl(spider2_cls)


#process.start()


#process.stop()
