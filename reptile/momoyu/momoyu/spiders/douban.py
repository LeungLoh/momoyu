import scrapy
from scrapy.selector import Selector
from momoyu.items import WbsiteItem
import re
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
            try:
                # subtitle=subtitle.decode('utf-8')
                nums= re.findall("\d+\.?\d*",subtitle)[0]
                uint = re.findall("\d+\.?\d*(\D{1})",subtitle)[0]
               
                
                if uint == "万":
                    nums=float(nums)*10000
                elif uint == "千":
                    nums=float(nums)*1000
                elif uint == "百":
                    nums=float(nums)*100
                elif uint == "十":
                    nums=float(nums)*10
                else:
                    nums=float(nums)
                
                item['subtitle']=str(int(nums))
            except Exception as err:
                item['subtitle']=""
            item['website']="douban"
            yield item

