import scrapy
from scrapy.selector import Selector
from momoyu.items import WbsiteItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['s.weibo.com/top/summary']
    start_urls = ['https://s.weibo.com/top/summary/']

    def parse(self, response):
        item = WbsiteItem()
        selector = Selector(response)
        articles = selector.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
        
        for article in articles:
            title = article.xpath('td[2]/a/text()').extract_first(default='')
            url = article.xpath('td[2]/a/@href').extract_first(default='')
            subtitle = article.xpath('td[2]/span/text()').extract_first(default='')
            item['title'] = title
            item['url'] = "https://s.weibo.com"+url
            try:
                item['subtitle'] =str(subtitle)
            except:
                item['subtitle'] =""
            item['website']=["weibo"]
            yield item

