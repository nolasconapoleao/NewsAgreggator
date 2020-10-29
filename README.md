# NewsAgreggator

## Generic crawler

Usage: `scrapy crawl Generic -o generic.json`

The result will be output to `file.json`

## Ctw and Bmw crawler
`$ cd ctwCrawler`

`$ scrapy crawl CtwAndBmw`

The result will be output to `NewsResult.txt`

## Crawler3

Allows per site configuration of patterns, url ignore strings, and regex filters
(not implemented yet)

Includes configurations for Público and Notícias ao Minuto.

Outputs json compatible with the Yammer Publisher script.

Usage: `scrapy crawl Crawler3 -o <output file name>`

## Yammer Publisher

###Get yammer access toke
    https://www.yammer.com/client_applications

###Publish to Yammer
    `$ python3 yammer_client.py
