from pathlib import Path

from scrapy.spiders import SitemapSpider
from ..items import CrawlerItem
from .helpers import *


class DatSpider(SitemapSpider):
    name = "dat"
    sitemap_urls = ["https://www.dat.de/sitemap.xml"]
    sitemap_rules = [
        ("/news/", "parse_news_and_dat_report"),
        ("/dat-report/", "parse_news_and_dat_report"),
        (".*", "parse")
    ]

    def parse(self, response):
        item = self.get_item(response)
        body = set_body('default', response)
        item["body"] = body
        item["hash"] = hash_body(body)
        yield item

    def parse_news_and_dat_report(self, response):
        item = self.get_item(response)
        body = set_body('news_and_dat_report', response)
        item["body"] = body
        item["hash"] = hash_body(body)
        yield item

    def get_item(self, response):
        item = CrawlerItem()
        item["path"] = response.url
        item["title"] = response.xpath('//title/text()').get()
        item["site_html"] = set_site_html(response)
        item["path_id"] = response.xpath('//body/@id').get()
        item["published_at"] = response.xpath('//time/@datetime').get()
        return item

