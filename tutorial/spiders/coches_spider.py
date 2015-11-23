import scrapy

class CochesSpider(scrapy.Spider):
    name = "coches"
    allowed_domains = ["www.coches.net"]
    start_urls = [
        "http://www.coches.net/coches-de-ocasion.aspx",
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@style="position:relative"]'):
            prefix='a/div[@class="datacar"]/div[@class="col2-grid"]/'
            precio = sel.xpath(prefix+'p[@class="preu floatleft"]/text()').extract()
            modelo = sel.xpath(prefix+'h2/text()').extract()
            provincia = sel.xpath(prefix+'p[@class="dades"]/span[@class="lloc"]/text()').extract()
            combustible =  sel.xpath(prefix+'p[@class="dades"]/span[@class="d3"]/text()').extract()
            year =  sel.xpath(prefix+'p[@class="dades"]/span[@class="d2"]/text()').extract()
            kms = sel.xpath(prefix+'p[@class="dades"]/span[@class="d1"]/text()').extract()
            datos = sel.xpath('div[@class="contact-ad"]').xpath('@data-t').extract()




            print precio, modelo, provincia, combustible, year, kms, datos

            prefix='a/div[@class="datacar_destacado"]/div[@class="col2-grid"]/'
            precio = sel.xpath(prefix+'p[@class="preu floatleft"]/text()').extract()
            modelo = sel.xpath(prefix+'h2/span/text()').extract()
            provincia = sel.xpath(prefix+'p[@class="dades"]/span[@class="lloc"]/span/text()').extract()
            combustible =  sel.xpath(prefix+'p[@class="dades"]/span[@class="d3"]/span/text()').extract()
            year =  sel.xpath(prefix+'p[@class="dades"]/span[@class="d2"]/span/text()').extract()
            kms = sel.xpath(prefix+'p[@class="dades"]/span[@class="d1"]/text()').extract()
            datos = sel.xpath('div[@class="contact-ad"]').xpath('@data-t').extract()
            print "--------------"

            print precio, modelo, provincia, combustible, year, kms, datos
            print "====================="

