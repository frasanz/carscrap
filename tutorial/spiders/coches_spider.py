import scrapy
import requests
from scrapy.http import Request
from tutorial.items import CochesItem

URL = "http://www.coches.net/coches-de-ocasion.aspx?pg=%d&OfferTypeGroup=0&or=-1&fi=SortDate"
starting_number = 0
number_of_pages = 5000 
class CochesSpider(scrapy.Spider):
    name = "coches"
    allowed_domains = ["www.coches.net"]
    start_urls = [URL % starting_number]
    def __init__(self):
        self.page_number = starting_number
    def start_requests(self):
        for i in range (self.page_number, number_of_pages, +1):
            yield Request(url = URL % i, callback=self.parse)

    def parse(self, response,i=0):
        for sel in response.xpath('//div[@id="dvResults"]/div/div'):
            item = CochesItem()
            item['modelo'] = sel.xpath('article/div/div/a/h2/span/text()').extract()
            item['precio'] = sel.xpath('article/div/div/a/div/div/strong/text()').extract()
            item['datos'] = sel.xpath('article/div/div/a/div/ul/li/text()').extract()
            yield item



