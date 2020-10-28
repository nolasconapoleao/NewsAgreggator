# -*- coding: utf-8 -*-
import scrapy

class GenericSpider(scrapy.Spider):
    name = 'Generic'

    start_urls = [
        'https://www.jn.pt',
        'https://www.dn.pt',
        'https://www.observador.pt',
        'https://www.rtp.pt/noticias',
        'https://www.noticiasaominuto.com',
        'https://www.publico.pt',
        'https://www.expresso.pt',
        'https://www.jornaldenegocios.pt',
    ]

    patterns = [
        "//a[contains(@href, 'covid')]/@href",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,
                                 callback=self.parse,
                                 cb_kwargs=dict(main_url=url)
                                 )

    def parse(self, response, main_url):
        #Search for text
        for links in [response.xpath(pattern).getall() for pattern in self.patterns]:
            yield {
                'domain': main_url,
                'url': links,
            }

        #for next_page_url in [response.xpath(pattern).extract_first() for pattern in self.patterns_url]:
        #    yield scrapy.Request(response.urljoin(next_page_url))
