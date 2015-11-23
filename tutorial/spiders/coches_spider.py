import scrapy
from tutorial.items import CochesItem

class CochesSpider(scrapy.Spider):
    name = "coches"
    allowed_domains = ["www.coches.net"]
    start_urls = [
        "http://www.coches.net/coches-de-ocasion.aspx",
    ]

    def parse(self, response):
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
        next_page = response.xpath('//a[@class="pnext"]/@href').extract()
        if next_page:
            url = response.urljoin("http://www.coches.net/coches-de-ocasion.aspx"+next_page[0])
            yield scrapy.Request(url,self.parse)



