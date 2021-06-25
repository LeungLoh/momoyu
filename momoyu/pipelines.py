# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from twisted.enterprise import adbapi
import time
import copy
class MysqlPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        # 从项目的配置文件中读取相应的参数
        cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", 'default')
        cls.HOST = crawler.settings.get("MYSQL_HOST", 'localhost')
        cls.PORT = crawler.settings.get("MYSQL_PORT", 3306)
        cls.USER = crawler.settings.get("MYSQL_USER", 'root')
        cls.PASSWD = crawler.settings.get("MYSQL_PASSWORD", '1234')
        return cls()

    def open_spider(self, spider):
        self.dbpool = adbapi.ConnectionPool('pymysql', host=self.HOST, port=self.PORT, user=self.USER, passwd=self.PASSWD, db=self.MYSQL_DB_NAME, charset='utf8')

    def close_spider(self, spider):
        self.dbpool.close()

    def process_item(self, item, spider):
        asynItem = copy.deepcopy(item)
        self.dbpool.runInteraction(self.insert_db, asynItem)
        return item

    def insert_db(self, tx, item):
        values =(
            item["title"],
            item["url"],
            item["subtitle"],
            item["website"],
            int(time.time())
        )
        insert_sql = """
            insert into momoyu(title,url,subtitle,website,date) values (%s,%s,%s,%s,%s)
        """
        # tx.execute(insert_sql, values)