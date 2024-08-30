
import scrapy

class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()
    author = scrapy.Field()
    published_date = scrapy.Field()
    url = scrapy.Field()

class EventItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
