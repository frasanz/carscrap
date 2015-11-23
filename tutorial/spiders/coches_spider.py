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
        for i in range (self.page_number, 5000, +1):
            yield Request(url = URL % i, callback=self.parse)

    def parse(self, response,i=0):
        for sel in response.xpath('//div[@style="position:relative"]'):
            item = CochesItem()
            prefix='a/div[@class="datacar"]/div[@class="col2-grid"]/'
            item['precio'] = sel.xpath(prefix+'p[@class="preu floatleft"]/text()').extract()
            item['modelo'] = sel.xpath(prefix+'h2/text()').extract()
            item['provincia'] = sel.xpath(prefix+'p[@class="dades"]/span[@class="lloc"]/text()').extract()
            item['combustible'] =  sel.xpath(prefix+'p[@class="dades"]/span[@class="d3"]/text()').extract()
            item['year'] =  sel.xpath(prefix+'p[@class="dades"]/span[@class="d2"]/text()').extract()
            item['kms'] = sel.xpath(prefix+'p[@class="dades"]/span[@class="d1"]/text()').extract()
            item['datos'] = sel.xpath('div[@class="contact-ad"]').xpath('@data-t').extract()

            if not item['precio']:
                prefix='a/div[@class="datacar_destacado"]/div[@class="col2-grid"]/'
                item['precio'] = sel.xpath(prefix+'p[@class="preu floatleft"]/text()').extract()
                item['modelo'] = sel.xpath(prefix+'h2/span/text()').extract()
                item['provincia'] = sel.xpath(prefix+'p[@class="dades"]/span[@class="lloc"]/span/text()').extract()
                item['combustible'] =  sel.xpath(prefix+'p[@class="dades"]/span[@class="d3"]/span/text()').extract()
                item['year'] =  sel.xpath(prefix+'p[@class="dades"]/span[@class="d2"]/span/text()').extract()
                item['kms'] = sel.xpath(prefix+'p[@class="dades"]/span[@class="d1"]/text()').extract()
            yield item



