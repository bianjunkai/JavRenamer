# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AvspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    vid = scrapy.Field()
    title = scrapy.Field()
    release_date = scrapy.Field()
    length = scrapy.Field()
    director = scrapy.Field()
    maker = scrapy.Field()
    label = scrapy.Field()
    cast = scrapy.Field()
    pic = scrapy.Field()

    pass
