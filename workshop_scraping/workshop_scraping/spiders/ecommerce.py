import scrapy

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/e-commerce/static']

    def parse(self, response):
        titles = []
        for resp in response.xpath('.//a/@title'):
            data = { "data" : resp.get()}
            titles.append(resp.get())
            yield data
        print("titles: ", titles)
