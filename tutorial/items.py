# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CochesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    modelo = scrapy.Field()
    price = scrapy.Field() 
    ciudad = scrapy.Field()
    combustible = scrapy.Field()
    year = scrapy.Field()
    kms = scrapy.Field()
