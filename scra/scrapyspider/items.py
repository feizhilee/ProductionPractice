# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_introduction = scrapy.Field()
    writer = scrapy.Field()
    publisher = scrapy.Field()
    price = scrapy.Field()
    book_grade = scrapy.Field()
    recommend_reason = scrapy.Field()
    book_type = scrapy.Field()
    pass
