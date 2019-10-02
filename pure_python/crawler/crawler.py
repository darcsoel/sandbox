import scrapy


class SomeCrawler(scrapy.Spider):
    name = 'some spider'
    allowed_domains = ['cactus-lviv.com/']
    start_urls = ['http://cactus-lviv.com/']

    def parse(self, response):
        for part in response.css:
            yield {'title': part.css('a ::text').extract_first()}

