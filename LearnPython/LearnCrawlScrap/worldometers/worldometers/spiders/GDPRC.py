import scrapy


class GdprcSpider(scrapy.Spider):
    name = 'GDPRC'
    allowed_domains = [
        'www.worldpopulationreview.com/']
    start_urls = [
        'https://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath(
            "(//table[@class='jsx-1487038798 table table-striped tp-table-body'])/tbody/tr")
        for row in rows:
            name = row.xpath(".//td[1]/a/text()").get()
            gdprc = row.xpath(".//td[2]/text()").get()
            population = row.xpath(".//td[3]/text()").get()

            yield {
                'country_name': name,
                'gdprc': gdprc,
                'population': population
            }
