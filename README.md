# momoyu

## 项目介绍
    该项目利用爬虫爬取各大论坛热搜，并且聚集展示，方便浏（摸）览（鱼）。

### 爬虫
    怕从使用的是scrapy的框架，对html使用xpath进行解析，得到对应的title、url、热度等信息，使用pipeline 入mysql。

### 后端
    后端使用的go+gin+gorm框架，提供一个简单的查询api

### 前端
    前端使用vue框架作为展示

## 爬取网站

-   [x] 豆瓣
-   [x] 微博
-   [x] oschina