# -*- coding: utf-8 -*-
import scrapy

class GenericSpider(scrapy.Spider):
    name = 'Generic'

    start_urls = [
        'https://jn.pt',
    ]

    patterns = [
        '//span/text()',
        '//div[@id="images"]/a/text()'
    ]

    patterns_url = [
        '//a[contains(@href, "ctw")]/@href',
        '//a[contains(@href, "Critical TechWorks")]/@href'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        #Search for text
        for quote in [response.xpath(pattern) for pattern in self.patterns]:
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

        for next_page_url in [response.xpath(pattern).extract_first() for pattern in self.patterns_url]:
            yield scrapy.Request(response.urljoin(next_page_url))
