from scrapy.crawler import CrawlerProcess
from p2p.crawler.spiders.link import LinkSpider
from scrapy.settings import Settings
from importlib import import_module
from scrapy.utils.project import get_project_settings
import sys
import os



settings = Settings()
settings_module_path = "settings"
if settings_module_path:
    settings.setmodule(settings_module_path, priority='project')
#s = import_module("..\\crawler\\settings.py")
process = CrawlerProcess(settings)

process.crawl(LinkSpider)

process.start()


process.stop()
