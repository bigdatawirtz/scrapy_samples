from urllib import response
import scrapy


class LibrosdelkoSpider(scrapy.Spider):
    name = "librosdelko"
    allowed_domains = ["www.librosdelko.com"]
    start_urls = ["https://www.librosdelko.com/collections/catalogo"]


    # Set maximum number of pages to scrape
    max_pages = 3
    pages_scraped = 0
    

    def parse(self, response):

        # Increment page counter
        self.pages_scraped += 1

        for book_link in response.css('p.title a::attr(href)').getall():
            absolute_link = response.urljoin(book_link)     
            yield response.follow(absolute_link, self.parse_book)   

        
        # Check if we should continue
        if self.pages_scraped < self.max_pages:

            # find tag a with text 'Siguiente'
            # add max depth to avoid infinite loop
            next_page = response.css('a:contains("Siguiente")::attr(href)').get()
            if next_page:
                absolute_next_page = response.urljoin(next_page)
                yield response.follow(absolute_next_page, self.parse)



    def parse_book(self, response):
        from scrapy_samples.items import BookItem
        import re

        book = BookItem()

        book['title'] = response.css('h1::text').get()
        book['author'] = response.css('p.vendor a::text').get()
        book['isbn'] = response.xpath('//li[contains(text(), "ISBN")]/text()').re_first(r'([\d-]+)')


        yield book
