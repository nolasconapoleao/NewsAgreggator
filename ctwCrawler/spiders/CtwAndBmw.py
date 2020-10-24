import scrapy

class CtwandbmwSpider(scrapy.Spider):
    name = 'CtwAndBmw'
    urls = [
        'https://www.jn.pt',
        'https://www.dn.pt',
        'https://www.observador.pt',
        'https://www.rtp.pt/noticias',
        'https://www.noticiasaominuto.com',
        'https://www.publico.pt',
        'https://www.expresso.pt',
        'https://www.jornaldenegocios.pt',
    ]

    patterns_url = [
        '//a[contains(@href, "bmw")]/@href',
        '//a[contains(@href, "BMW")]/@href',
        '//a[contains(@href, "ctw")]/@href',
        '//a[contains(@href, "Ctw")]/@href',
        '//a[contains(@href, "critical-techworks")]/@href',
        '//a[contains(@href, "criticaltechworks")]/@href',
    ]

    def prepend(self, title):
        switcher = {
            'Jornal de Notícias': "https://www.jn.pt",
            'Diário de Notícias': "https://www.dn.pt",
            'PÚBLICO — Pense bem, pense Público': "https://www.publico.pt",
            'Expresso | Liberdade para pensar': "https://www.expresso.pt",
            'Negócios: Cotações, Mercados, Economia, Empresas': "https://www.jornaldenegocios.pt",
        }
        return switcher.get(title, "")

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        siteTitle = response.css('title::text').extract_first()
        prefix = self.prepend(title=siteTitle)

        with open('NewsResult.txt', 'a') as f:
            inserted = []
            for pattern in self.patterns_url:
                links = response.xpath(pattern).getall()

                for link in links:
                    if link not in inserted and '#comments' not in link:
                        inserted.append(link)
                        f.write(prefix + link + '\n')
                        yield {
                            "link": prefix + link,
                        }
