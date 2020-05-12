import scrapy


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
        all_div_quote = response.css('div.quote')
        quote = all_div_quote.css('span.text::text').extract()
        author = all_div_quote.css('small.author::text').extract()
        tags = all_div_quote.css('a.tag::text').extract()
        yield {
            'quote': quote,
            'author': author,
            'tags': tags
        }
