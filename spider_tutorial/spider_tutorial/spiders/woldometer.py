import scrapy


class WoldometerSpider(scrapy.Spider):
    name = "woldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = [
        "https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        country_links = response.xpath('//td/a')

        for country in country_links[1:2]:
            country_name = country_links.xpath(".//text()").get()
            link = country.xpath('.//@href').get()

            yield response.follow(url=link, callback=self.parse_country, meta={'country': country_name})

    def parse_country(self, response):
        country = response.request.meta
        rows = response.xpath(
            "(//table[contains(@class, 'table')])[1]/tbody/tr")
        _response[str(country)] = []

        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            _response[str(country)].append(
                {'year': year, 'population': population})

        yield {
            [country]: {

            }
        }
