# -*- coding: utf-8 -*-
# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
from pymongo import MongoClient


class ZhilianPipeline(object):
    #初始化数据库
    def __init__(self):
        # 获取主机名、端口号和数据库名称
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        # 创建数据库连接
        self.client = MongoClient(host=host, port=port)
        # 指向指定数据库
        mdb=self.client[dbname]
        #获取数据库中的表
        self.post=mdb[settings['MONGODB_DOCNAME']]
    def process_item(self,item,spider):
        data=dict(item)
        #向数据表中添加数据
        self.post.insert(data)
        return item
    def close_spider(self,spider):
        #爬虫关闭，关闭数据库连接
        self.client.close()




