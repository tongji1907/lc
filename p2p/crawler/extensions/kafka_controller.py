__author__ = 'wuyan'
import os
#from six.moves import cPickle as pickle
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer
from kafka.common import OffsetOutOfRangeError
from scrapy import signals
#from scrapy.utils.job import job_dir


class KafkaController(object):
    """Store and load spider state during a scraping job"""

    def __init__(self, crawler):

        self.crawler = crawler
        self.kafka_conn = KafkaClient('120.25.216.93:9092')

        crawler.signals.connect(self.spiderIdle, signal=signals.spider_idle)
        #crawler.signals.connect(self.engine_stopped, signal=signals.engine_stopped)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def spider_closed(self, spider):
        None

    def spiderIdle(self, spider):
        print "OK 123"

