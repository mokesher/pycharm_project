# -*- coding: utf-8 -*-
import scrapy


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['dig.chouti.com']
    start_urls = ['https://dig.chouti.com/']

    def parse(self, response):
        # print(response)
        data_list = response.xpath('//a[@class="link-title link-statistics"]')
        for item in data_list:
            text = item.xpath('.//text()').extract_first()
            href = item.xpath('.//@href').extract_first()
            print(text, href)
