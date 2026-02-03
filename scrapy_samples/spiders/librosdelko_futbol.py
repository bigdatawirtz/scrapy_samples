import scrapy


class LibrosdelkoFutbolSpider(scrapy.Spider):
    name = "librosdelko_futbol"
    allowed_domains = ["www.librosdelko.com"]
    start_urls = ["https://www.librosdelko.com/collections/catalogo/futbol"]

    def parse(self, response):
        for book_link in response.css('p.title a::attr(href)').getall():
            absolute_link = response.urljoin(book_link)     
            yield response.follow(absolute_link, self.parse_book)   

    def parse_book(self, response):
        from scrapy_samples.items import BookItem
        import re

        book = BookItem()

        book['title'] = response.css('h1::text').get()
        book['author'] = response.css('p.vendor a::text').get()
        #isbn_text = response.xpath('//li[contains(text(), "ISBN")]/text()').get()
        #book['isbn'] = re.search(r'(\d+-\d+-\d+-\d+-\d+)', isbn_text).group(1)

        # ✅ One-line fix - use .re_first() instead
        book['isbn'] = response.xpath('//li[contains(text(), "ISBN")]/text()').re_first(r'([\d-]+)')


        yield book
