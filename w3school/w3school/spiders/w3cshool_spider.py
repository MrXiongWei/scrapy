#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log

from w3school.items import W3SchoolItem


class W3schoolSpider(Spider):
    """爬取w3school标签"""
    # log.start("log",loglevel='INFO')
    name = "w3school"
    allowed_domains = ["w3school.com.cn"]
    start_urls = [
        "http://www.w3school.com.cn/xml/xml_syntax.asp"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@id="navsecond"]/div[@id="course"]/ul[1]/li')
        items = []
        for site in sites:
            item = W3SchoolItem()

            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('a/@title').extract()

            for t in title:
                item['title'] = t
            for l in link:
                item['link'] = l
            for d in desc:
                item['desc'] = d
            # item['title'] = [t.encode('utf-8') for t in title]
            # item['link'] = [l.encode('utf-8') for l in link]
            # item['desc'] = [d.encode('utf-8') for d in desc]
            items.append(item)

            # 记录
            log.msg("Appending item...", loglevel='INFO')

        log.msg("Append done.", loglevel='INFO')
        return items
