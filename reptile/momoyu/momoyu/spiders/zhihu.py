import scrapy
from scrapy.selector import Selector
from momoyu.items import WbsiteItem
import json

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true']
    start_urls = ['https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true']

    def parse(self, response):
        item = WbsiteItem()
        articles=json.loads(response.text)
        # selector = Selector(response)
        # articles = selector.xpath('//*[@id="TopstoryContent"]/div/div/div[2]')

        for article in articles["data"]:
            title = article["target"]["title"]
            url = article["target"]["url"]
            subtitle = article["detail_text"]


            item['title'] = title
            item['url'] = url
            item['subtitle'] = subtitle
            item['website']="zhihu"
            yield item
