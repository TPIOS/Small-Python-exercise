from scrapy.spiders import SitemapSpider
class MySpider(SitemapSpider):
    def parse_electronics(self, response):
        return
    
    def parse_apparel(self, response):
        return

    sitemap_urls = ['http://www.example.com/sitemap.xml']
    sitemap_rules = [('/electronics/', parse_electronics), ('/apparel/',parse_apparel),]
