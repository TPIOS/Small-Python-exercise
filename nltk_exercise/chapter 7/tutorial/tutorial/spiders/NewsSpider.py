from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item, Field
import scrapy

class NewsItem(scrapy.Item):
    title = Field()
    topic = Field()
    desc = Field()

class NewsSpider(CrawlSpider):
    name = "news"
    allowed_domains = ["news.google.com"]
    start_urls = [
        "https://news.google.com"
    ]

    rules = (
        Rule(LinkExtractor(allow=('cnn.com',), deny=('http://edition.cnn.com/',))),
        Rule(LinkExtractor(allow=('news.google.com',)), callback="parse_news_item"),
        )

    def parse(self, response):
        sel = Selector(response)
        item = NewsItem()
        item['title'] = sel.xpath('//title/text()').extract()
        item['topic'] = sel.xpath('/div[@class="topic"]').extract()
        item['desc'] = sel.xpath('//td/text()').extract()

        return item

        # filename = "leetcode.txt"
        # open(filename, 'wb').write(response.body)
    