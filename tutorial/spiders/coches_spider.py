import scrapy

class CochesSpider(scrapy.Spider):
    name = "coches"
    allowed_domains = ["www.coches.net"]
    start_urls = [
        "http://www.coches.net/coches-de-ocasion.aspx",
    ]

    def parse(self, response):
        precio = response.xpath('//p[@class="preu floatleft"]/text()').extract()
        modelo = response.xpath('//div[@class="col2-grid"]//h2/text()').extract()
        provincia = response.xpath('//span[@class="lloc"]/text()').extract()
        combustible =  response.xpath('//span[@class="d3"]/text()').extract()
        year =  response.xpath('//span[@class="d2"]/text()').extract()
        kms = response.xpath('//span[@class="d1"]/text()').extract()
        datos = response.xpath('//div[@class="contact-ad"]').extract()


        print modelo, precio, provincia, combustible, year, kms, datos
