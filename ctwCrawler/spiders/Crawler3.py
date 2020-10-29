import scrapy
from urllib.parse import urljoin

class Crawler3(scrapy.Spider):
    name = 'Crawler3'

    class SiteInfo:
        def __init__(self, name, url, patterns, ignore = None, regex = None):
            self.name = name
            self.url = url
            self.patterns = patterns
            self.regex = regex
            self.ignore = ignore

    sites = [
        SiteInfo(
            u"Público".encode('utf-8').decode('utf-8'),
            'https://www.publico.pt/pesquisa?query=critical+techworks',
            [
                "//div[@class='media-object-section']/a[@href]/@href"
            ],
            ignore = [
                '#comments'
            ]
        ),
        SiteInfo(
            u"Notícias ao Minuto".encode('utf-8').decode('utf-8'),
            'https://www.jornaldenegocios.pt/pesquisa/?SearchRequest.Query=critical+techworks',
            [
                "//article//h2/a[@href]/@href"
            ],
            ignore = [
                '#comments'
            ]
        ),
    ]

    default_patterns = [
        '//a[contains(@href, "bmw")]/@href',
        '//a[contains(@href, "BMW")]/@href',
        '//a[contains(@href, "ctw")]/@href',
        '//a[contains(@href, "Ctw")]/@href',
        '//a[contains(@href, "critical-techworks")]/@href',
        '//a[contains(@href, "criticaltechworks")]/@href',
    ]

    def start_requests(self):
        for site in self.sites:
            print('crawling ' + site.name + '...')
            request = scrapy.Request(url=site.url, callback=self.parse)
            request.meta['site'] = site
            yield request

    def parse(self, response):
        site = response.meta['site']
        prefix = site.name

        inserted = []

        if len(site.patterns) > 0:
            print('[' + site.name + '] using site patterns')
            patterns = site.patterns
        else:
            print('[' + site.name + '] using default patterns')
            patterns = self.default_patterns

        for pattern in patterns:
            links = response.xpath(pattern).getall()
        
        print('[' + site.name + '] got ' + str(len(links)) + ' links')

        for link in links:
            link = urljoin(site.url, link)
            if link not in inserted and not any(ele in link for ele in site.ignore):
                print('[' + site.name + '] inserting "' + link + '"...')
                inserted.append(link)
            else:
                print('[' + site.name + '] ignoring "' + link + '"...')

        yield {
            'domain': '',
            'url': inserted,
        }
