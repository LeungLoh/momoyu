import scrapy
from scrapy.selector import Selector
from momoyu.items import WbsiteItem

class OschinaSpider(scrapy.Spider):
    name = 'oschina'
    allowed_domains = ['oschina.net']
    start_urls = ['https://www.oschina.net/']

    def parse(self, response):
        item = WbsiteItem()
        selector = Selector(response)
        articles = selector.xpath('//*[@id="mainScreen"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div[11]/div/div[2]/div[2]/div')
        for article in articles:
            title = article.xpath('a/text()').extract_first(default='')
            url = article.xpath('a/@href').extract_first(default='')
            subtitle = article.xpath('div/text()').extract_first(default='')
            item['title'] = title
            item['url'] = url
            item['subtitle'] = subtitle
            item['website']="oschina"
            yield item

