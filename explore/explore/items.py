# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class cover(scrapy.Item):
    title = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()

class ExploreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
