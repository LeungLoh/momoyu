import scrapy

class WbsiteItem(scrapy.Item):
   title = scrapy.Field()
   subtitle = scrapy.Field()
   url=scrapy.Field()
   website=scrapy.Field()