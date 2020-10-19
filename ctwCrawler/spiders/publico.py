import scrapy

class PublicoSpider(scrapy.Spider):
    name = 'publico'

    def start_requests(self):
        urls = [
            'https://www.publico.pt/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        with open('ctw-result.txt', 'w') as f:
            for article in response.xpath('//a[@class="card__faux-block-link"][contains(@href, "ctw")]'):
                text = article.css('a::text').getall()[0]
                link = article.xpath('@href').getall()[0]
                f.write(text)
                f.write("https://www.publico.pt"+link)
                f.write("\n")
                yield {
                    "text": text,
                    "link": link,
                }

        # TODO: Go to next page