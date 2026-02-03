import scrapy
from scrapy_samples.items import BookItem


class BookSpider(scrapy.Spider):
    name = 'books'
    
    # Two similar book pages to scrape
    start_urls = [
        'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
        'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
    ]
    
    def parse(self, response):
        """Extract book information using BookItem"""
        
        # Create a new BookItem instance
        book = BookItem()
        
        # Extract data from the page
        book['title'] = response.css('h1::text').get()
        book['price'] = response.css('.price_color::text').get()
        book['availability'] = response.css('.availability::text').re_first(r'\(.*\)')
        
        # Extract rating (star-rating class contains the rating)
        rating_class = response.css('.star-rating::attr(class)').get()
        book['rating'] = rating_class.replace('star-rating ', '') if rating_class else 'No rating'
        
        # Yield the item (Scrapy will process it)
        yield book
