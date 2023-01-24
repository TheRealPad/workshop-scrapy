import scrapy

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/e-commerce/static']

    def parse(self, response):
        titles = []
        detail_link = []
        description = []
        price = []
        image = []
        rating = []
        review = []
        for resp in response.xpath('.//a/@title'):
            data = { "data" : resp.get()}
            titles.append(resp.get())
            yield data
        for resp in response.xpath('.//a/@title'):
            data = { "data" : resp.get()}
            detail_link.append(resp.get())
            yield data
        for resp in response.xpath('.//p/@description'):
            data = { "data" : resp.get()}
            description.append(resp.get())
            yield data
        print("titles: ", titles)
        print("detail link: ", detail_link)
        print("description: ", description)
        print("price: ", price)
        print("image: ", image)
        print("rating: ", rating)
        print("review: ", review)
