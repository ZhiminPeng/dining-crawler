# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DiningItem(scrapy.Item):
    # define the fields for your item here like:
    # hall_name = scrapy.Field()
    menu = scrapy.Field()
    hall_name = scrapy.Field()
    favor = scrapy.Field()
    link = scrapy.Field()
