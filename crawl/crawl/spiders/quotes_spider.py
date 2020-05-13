import scrapy
from ..items import CrawlItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = CrawlItem()
        all_div_quote = response.css('div.quote')

        # to capture all data from one container at a time
        for data in all_div_quote:
            quote = data.css('span.text::text').extract()
            author = data.css('small.author::text').extract()
            tags = data.css('a.tag::text').extract()

            items['quote'] = quote
            items['author'] = author
            items['tags'] = tags

            yield items
        
