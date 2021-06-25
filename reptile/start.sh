#!/bin/bash
# 0 * * * * cd /root/workspace/momoyu/reptile && sh start.sh >> replite.log 2>&1
cd momoyu
echo $PWD
scrapy crawl douban
scrapy crawl zhihu 
scrapy crawl weibo 
scrapy crawl oschina