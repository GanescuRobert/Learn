import scrapy


class OferteSpider(scrapy.Spider):
    name = 'oferte'
    allowed_domains = ['www.olx.ro']
    start_urls = ['https://www.olx.ro/oferte/']

    def parse(self, response):
        pass
