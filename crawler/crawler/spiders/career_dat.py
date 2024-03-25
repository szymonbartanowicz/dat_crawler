from pathlib import Path
from scrapy.spiders import SitemapSpider
from ..items import CrawlerItem
from .helpers import *


class DatSpider(SitemapSpider):
    name = "career_dat"
    sitemap_urls = ["https://career.dat.de/sitemap.xml"]

    def parse(self, response):
        try:
            item = CrawlerItem()
            item["path"] = response.url
            item["title"] = response.xpath('//title/text()').get()
            item["site_html"] = set_site_html(response)
            item["path_id"] = response.xpath('//body/@id').get()
            item["published_at"] = parse_to_db_datetime(
                response.xpath("//meta[contains(@itemprop, 'datePosted')]/@content").get())
            item["valid_through"] = parse_to_db_datetime(
                response.xpath("//meta[contains(@itemprop, 'validThrough')]/@content").get())
            item["hiring_organization"] = response.xpath(
                "//meta[contains(@itemprop, 'hiringOrganization')]/@content").get()
            body = set_body(response, 'job_offer')
            item["body"] = body
            item["hash"] = hash_body(body)
            yield item
        except Exception as e:
            print(f'Something went wrong for url {response.url}: {e}')


