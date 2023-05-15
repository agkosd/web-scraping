import scrapy

class WoldometerSpider(scrapy.Spider):
    name = "woldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        country_links = response.xpath('//td/a')

        list = []
        for link in country_links:
            country_name = link.xpath('.//text()').get()
            link = link.xpath('.//@href').get()
            list.append({'country_name':country_name, 'link':response.urljoin(link)})
            
        yield{
            'country-links':list
        }