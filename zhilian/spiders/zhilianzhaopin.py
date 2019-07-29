# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from zhilian.items import ZhilianItem
class ZhilianSpider(scrapy.Spider):
    name = 'zhilianzhaopin'             #定义了Scrapy如何定位(并初始化)spider
    allowed_domains = ['zhaopin.com']        #允许爬取的域名(domain)列表(list)
    start_urls = ['http://zhaopin.com/']   #指定URL列表
    def start_requests(self):       #spider用于爬取的第一个Request
        for i in range(0, 40):
            for a in range(-1, 10):
                url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90\
        		&cityId=489&workExperience=-1&education={}&companyType\
        		=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3'.format(i * 90, a)
            yield Request(url=url,callback=self.parse)

    def parse(self, response):      #处理下载的response的默认方法
        result = json.loads(response.text)
        results = result['data']['results']
        item = ZhilianItem()
        for items in results:
            item['jobName'] = items['jobName']
            item['salary'] = items['salary']
            item['welfare'] = items['welfare']
            item['url'] = items['positionURL']
            item['city_display'] = items['city']['display']
            item['company'] = items['company']['name']
            item['company_size'] = items['company']['size']['name']
            item['company_type'] = items['company']['type']['name']
            item['emplType'] = items['emplType']
            item['eduLevel'] = items['eduLevel']['name']
            item['updateDate'] = items['updateDate']
            item['workingExp'] = items['workingExp']['name']
            yield item

















