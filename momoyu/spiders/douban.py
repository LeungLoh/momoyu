import scrapy
from scrapy.selector import Selector
from momoyu.items import WbsiteItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com//']

    def parse(self, response):
        item = WbsiteItem()
        selector = Selector(response)
        articles = selector.xpath('//*[@id="anony-sns"]/div/div[2]/div[2]/ul/div/ul/li')
        for article in articles:
            title = article.xpath('a/text()').extract_first(default='')
            url = article.xpath('a/@href').extract_first(default='')
            subtitle = article.xpath('span/text()').extract_first(default='')
            item['title'] = title
            item['url'] = url
            item['subtitle'] = subtitle
            item['website']="douban"
            yield item

