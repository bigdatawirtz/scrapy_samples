import scrapy


class CapitanswingBigdataSpider(scrapy.Spider):
    name = "capitanswing_bigdata"
    allowed_domains = ["capitanswing.com"]
    start_urls = ["https://capitanswing.com/tematicas/big-data/"]

    def parse(self, response):
        
        for book_link in response.css('a.book-link::attr(href)').getall():
            yield response.follow(book_link, self.parse_book)   

    def parse_book(self, response):
        from scrapy_samples.items import BookItem
        import re

        book = BookItem()

        book['title'] = response.css('h2 strong::text').get()
        book['author'] = response.css('h5 a::text').get()
        
        isbn_text = response.css('div.col-auto div::text').get()
        book['isbn'] = re.search(r'(\d+-\d+-\d+-\d+-\d+)', isbn_text).group(1)

        yield book
