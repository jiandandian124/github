
import time
import scrapy
from scrapy import item
from scrapy.http import request
from msds.items import MsdsItem
from pymongo import MongoClient
from pymongo import InsertOne
# scrapy crawl msds02 -o text2.csv
#接下来要测试ip的更换
#未完成的任务：1.CAS爬取格式不对，需要修改(已经解决)
#               1.1.分子式爬取格式不对
#             2.验证url的代码没写 (已经写了)
#             3.还没有连接数据库，数据没有存入
#             4.“其他”还没有爬取(差不多解决了)
#             5.ip更换还没有测试
#             6.‘其他’放在mongodb里，剩下的放进mysql里
#             7.当无法爬取时，能够及时停止
class Msds01Spider(scrapy.Spider):
    name = 'msds02'
    allowed_domains = ['china.guidechem.com']
    start_urls = ['https://china.guidechem.com/datacenter/msds/c/699.html']
    
    def insert_s(self,numb):                               #第2个函数进入
        #连接数据库
        conn = MongoClient('localhost',maxPoolSize=None)
        my_db = conn['msds']
        my_aa = my_db['urls']
        jilu = my_aa.find({'id' : numb})
        for x in jilu:                                      # x是字典类型
            a = x['state']                                  #取x的state键值   
            if a == '1' :                                   #state为1 是没有爬取，0则为爬取过
                b = x['url']                                               #取x的url键值
                return b                                    #成功取得url
            else:
                return 0                                    #失败返回0

    def update_state(self,numb):                            #第4个函数进入
        conn = MongoClient('localhost',maxPoolSize=None)
        my_db = conn['msds']
        my_aa = my_db['urls']
        myquery = { "id": numb }                             #修改id为当前数字的state状态为0
        newvalues = { "$set": { "state": "0" } }    
        my_aa.update_one(myquery, newvalues)

    def parse(self, response):                               #第一个函数进入
        #699,10985
        for i in range(699,702):
            
            nemb = i
            ne = self.insert_s(nemb)
            if ne == '0' :
                continue                                     #判断返回值，为0则跳出单次循环
            ur = response.urljoin(ne)
            time.sleep(5)                                     #休眠5秒
            request = scrapy.Request(url=ur, callback=self.parse_s, meta={'id':nemb})
            yield request 
    def parse_s(self, response):                               #第3个函数进入
        item = MsdsItem()
        msds_list = []
        for i in range(1,16):
            hraf = '//table[@bgcolor="#CADBEF"]//tr[%d]/td[2]/text()'%(i)
            a =  response.xpath(hraf).extract()[0].strip()
            if not a :
                a = '暂无数据'
            msds_list.append(a)
        # print(msds_list)
        numb = 600
        numb = response.meta['id']     #接受参数
        self.update_state(numb)

        item['id'] = numb
        item['国标编号'] = msds_list[0]
        item['CAS'] = response.xpath('//table[@bgcolor="#CADBEF"]//tr[2]/td[2]/a/text()').extract()[0].strip()
        item['中文名称'] = msds_list[2]
        item['英文名称'] = msds_list[3]
        item['别名'] = msds_list[4]
        item['分子式'] = response.xpath('//table[@bgcolor="#CADBEF"]//tr[6]/td[2]').extract()[0].strip()
        item['分子量'] = msds_list[6]
        item['熔点'] = msds_list[7]
        item['密度'] = msds_list[8]
        item['蒸汽压'] = msds_list[9]
        item['溶解性'] = msds_list[10]
        item['稳定性'] = msds_list[11]
        item['外观与性状'] = msds_list[12]
        item['危险标记'] = msds_list[13]
        item['用途'] = msds_list[14]
        item['其他'] = response.xpath('//td[@colspan="2"]//font[@size="2"]/text()').extract()
        yield item
    