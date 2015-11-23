# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CochesItem(scrapy.Item):
    # define the fields for your item here like:
    modelo = scrapy.Field()
    precio = scrapy.Field() 
    provincia = scrapy.Field()
    combustible = scrapy.Field()
    year = scrapy.Field()
    kms = scrapy.Field()
    datos = scrapy.Field()
