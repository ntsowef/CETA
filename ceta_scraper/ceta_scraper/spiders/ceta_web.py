# ceta_scraper/spiders/ceta_spider.py

import scrapy
from ..items import ArticleItem, EventItem
from scrapy.crawler import CrawlerProcess
import pandas as pd

class CetaSpider(scrapy.Spider):
    name = "ceta_spider"
    allowed_domains = ["ceta.org.za"]
    start_urls = ["https://www.ceta.org.za/"]

    custom_settings = {
        'FEEDS': {
            'articles.csv': {'format': 'csv', 'overwrite': True},
            'events.csv': {'format': 'csv', 'overwrite': True},
        }
    }

    def parse(self, response):
        # Scrape articles
        for article in response.xpath('//div[contains(@class, "article")]'):
            item = ArticleItem()
            item['title'] = article.xpath('.//h2/text()').get()
            item['body'] = ' '.join(article.xpath('.//p/text()').getall())
            item['author'] = article.xpath('.//span[@class="author"]/text()').get()
            item['published_date'] = article.xpath('.//span[@class="date"]/text()').get()
            item['url'] = response.urljoin(article.xpath('.//a/@href').get())
            yield item

        # Follow pagination links for articles
        next_page = response.xpath('//a[contains(@class, "next")]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

        # Scrape events
        for event in response.xpath('//div[contains(@class, "event")]'):
            item = EventItem()
            item['name'] = event.xpath('.//h3/text()').get()
            item['description'] = ' '.join(event.xpath('.//p/text()').getall())
            item['date'] = event.xpath('.//span[@class="date"]/text()').get()
            item['location'] = event.xpath('.//span[@class="location"]/text()').get()
            item['url'] = response.urljoin(event.xpath('.//a/@href').get())
            yield item

        # Follow pagination links for events
        next_event_page = response.xpath('//a[contains(@class, "next-events")]/@href').get()
        if next_event_page:
            yield response.follow(next_event_page, self.parse)
