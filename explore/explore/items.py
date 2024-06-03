# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class cover(Item):
    title = Field()
    file_urls = Field()
    files = Field()

class ExploreItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
