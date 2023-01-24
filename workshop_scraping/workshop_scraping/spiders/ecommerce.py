import scrapy


class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = ['http://webscraper.io/test-sites/']

    def parse(self, response):
        for resp in response.xpath('.//a/text()'):
            data = { "data" : resp.get()}
            yield data
