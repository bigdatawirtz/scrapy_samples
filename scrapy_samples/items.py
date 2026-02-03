import scrapy


class BookItem(scrapy.Item):
    """Item for storing book information"""
    title = scrapy.Field()
    author = scrapy.Field()
    isbn = scrapy.Field()

