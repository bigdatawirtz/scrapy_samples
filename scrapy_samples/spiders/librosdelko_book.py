import scrapy

import re
from scrapy_samples.items import BookItem

class LibrosdelkoBookSpider(scrapy.Spider):
    name = "librosdelko_book"
    allowed_domains = ["www.librosdelko.com"]
    start_urls = ["https://www.librosdelko.com/products/nos-parece-mejor"]

    def parse(self, response):
        book = BookItem()

        book['title'] = response.css('h1::text').get()
        book['author'] = response.css('p.vendor a::text').get()
        isbn_text = response.xpath('//li[contains(text(), "ISBN")]/text()').get()
        book['isbn'] = re.search(r'(\d+-\d+-\d+-\d+-\d+)', isbn_text).group(1)


        yield book