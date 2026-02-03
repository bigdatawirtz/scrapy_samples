# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



class ValidateItemPipeline:
    """Pipeline to validate items before saving"""
    
    def process_item(self, item, spider):
        """Check if item has required fields"""
        required_fields = ['title', 'author', 'isbn']
        
        for field in required_fields:
            if field not in item or not item[field]:
                spider.logger.warning(f"Item missing {field}: {item}")
                raise DropItem(f"Missing {field} in {item}")
        
        spider.logger.info(f"Validated item: {item['title']}")
        return item


class UppercaseTitlePipeline:
    """Pipeline to convert book titles to uppercase"""
    
    def process_item(self, item, spider):
        """Convert title to uppercase"""
        if 'title' in item:
            item['title'] = item['title'].upper()
            spider.logger.info(f"Converted title to uppercase: {item['title']}")
        return item

class SaveToFilePipeline:
    """Pipeline to save items to a JSON file"""
    
    def open_spider(self, spider):
        """Called when spider opens - initialize the file"""
        import json
        self.file = open('books_output.json', 'w', encoding='utf-8')
        self.items = []
        spider.logger.info("Opened output file")
    
    def close_spider(self, spider):
        """Called when spider closes - write all items and close file"""
        import json
        json.dump(self.items, self.file, indent=2, ensure_ascii=False)
        self.file.close()
        spider.logger.info(f"Saved {len(self.items)} items to file")
    
    def process_item(self, item, spider):
        """Add item to the list"""
        self.items.append(dict(item))
        return item


# Exception for dropping invalid items
from scrapy.exceptions import DropItem