# -*- coding: utf-8 -*-
BOT_NAME = 'zhilian'

SPIDER_MODULES = ['zhilian.spiders']
NEWSPIDER_MODULE = 'zhilian.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhilian.pipelines.ZhilianPipeline': 300,
}
#monogodb本机连接地址
MONGODB_HOST='127.0.0.1'
#端口号
MONGODB_PORT=27017
#设置数据库名称
MONGODB_DBNAME='ZHILIAN'
#存放数据的表名称
MONGODB_DOCNAME='jobs'

#将爬取到的数据进行序列化并通过csv表格形式进行存储
FEED_EXPORT_FIELDS = ['jobName','salary', 'welfare','url',\
                      'city_display','company','company_size',\
                      'company_type','emplType','eduLevel','updateDate','workingExp']
FEED_EXPORT_ENCODING = 'GB2312'     #定义编码类型
FEED_FORMAT = 'CSV' # 保存为csv文件
