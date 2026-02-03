from urllib import response
import scrapy
import re

from scrapy_samples.items import BookItem

class CapitanswingBookSpider(scrapy.Spider):
    name = "capitanswing_book"
    allowed_domains = ["capitanswing.com"]
    start_urls = ["https://capitanswing.com/libros/armas-de-destruccion-matematica/"]

    def parse(self, response):
        
        book = BookItem()

        book['title'] = response.css('h2 strong::text').get()
        book['author'] = response.css('h5 a::text').get()
        
        isbn_text = response.css('div.col-auto div::text').get()
        book['isbn'] = re.search(r'(\d+-\d+-\d+-\d+-\d+)', isbn_text).group(1)

        yield book
