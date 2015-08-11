#!/usr/bin/env python
from scrapy.crawler import CrawlerProcess
#from p2p.crawler.spiders.link import LinkSpider
#from p2p.crawler.spiders.link2 import Link2Spider
from scrapy.settings import Settings
from importlib import import_module
from scrapy.utils.project import get_project_settings
import sys
import os
from scrapy.utils.misc import load_object



settings = Settings()
settings_module_path = "settings"
if settings_module_path:
    settings.setmodule(settings_module_path, priority='project')
#s = import_module("..\\crawler\\settings.py")
process = CrawlerProcess(settings)

linkSpider = 'p2p.crawler.spiders.link.LinkSpider'
linkSpider2 = 'p2p.crawler.spiders.link2.Link2Spider'
spider_cls = load_object(linkSpider)
spider2_cls = load_object(linkSpider2)
process.crawl(spider_cls)

process.crawl(spider2_cls)

process.start()


#process.stop()
