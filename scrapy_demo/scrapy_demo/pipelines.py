# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import json

class ScrapyAcfun(object):

    def __init__(self, path):
        self.f = None
        self.path = path

    def process_item(self,item,spider):
        text = dict(item)
        for key,value in text.items():
            self.f.write(str(key) + ":" + str(value).strip())
            self.f.write("\n")
        self.f.write("\n")
        return item

    @classmethod
    def from_crawler(cls, crawler):
        path = crawler.settings.get('HREF_FILE_PATH')
        print(path)
        return cls(path)

    def open_spider(self,spider):
        print("open")
        self.f = open(self.path,'a+')

    def close_spider(self,spider):
        print("close")
        self.f.close()




class ScrapyAcfunSql(object):
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root",password="root",database="spider",charset="utf8")
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        print(item)
        result = self.cursor.execute("SELECT content from acfun WHERE content=%s;", [item["content"]])
        if not result:
            self.cursor.execute("insert into acfun(article_title,page,content,url,date) values(%s,%s,%s,%s,%s)", [item["article_title"],item["page"],item["content"],item["url"],item["date"]])
            self.conn.commit()

        return item

