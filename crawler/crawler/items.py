# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    path = scrapy.Field()
    path_id = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    site_html = scrapy.Field()
    published_at = scrapy.Field()
    hash = scrapy.Field()
    valid_through = scrapy.Field()
    hiring_organization = scrapy.Field()
