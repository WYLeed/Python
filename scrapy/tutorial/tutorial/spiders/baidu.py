# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.org']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
