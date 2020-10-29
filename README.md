# NewsAgreggator

## Requirements
    $ pip3 install scrapy
    $ pip3 install yampy

## Generic crawler

Usage: `scrapy crawl Generic -o generic.json`

The result will be output to `generic.json`

## Ctw and Bmw crawler

`$ scrapy crawl CtwAndBmw`

The result will be output to `NewsResult.txt`

## Crawler3

Allows per site configuration of patterns, url ignore strings, and regex filters
(not implemented yet)

Includes configurations for Público and Notícias ao Minuto.

Outputs json compatible with the Yammer Publisher script.

Usage: `scrapy crawl Crawler3 -o <output file name>.json`

## Yammer Publisher

###Get yammer access token
    https://www.yammer.com/client_applications

###Publish to Yammer
    $ python3 ctwCrawler/publisher/yammer_client.py
