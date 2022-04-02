import time
from typing import Text
import scrapy
from scrapy import item
from msds.items import MsdsItem
import pandas as pd

# scrapy crawl msds01 -o text.csv
class Msds01Spider(scrapy.Spider):
    name = 'msds01'
    allowed_domains = ['china.guidechem.com']
    start_urls = ['https://china.guidechem.com/datacenter/msds_cn_list-p1.html']
    
    def parse(self, response):

        #/html/body/div[2]/div[4]/div[2]/table/tbody/tr/td[3]/table[3]/tbody/tr[1]/td[1]/a
        ttrrs = response.xpath('//table[@class="bk"]//tr')
        
        for ttrr in ttrrs :
            ttdds = ttrr.xpath('./td')
            for ttdd in ttdds :
                time.sleep(5)
                #item = MsdsItem()
                text = ttdd.xpath('./a/@href').extract()[0]
                #u = response.urljoin(text)
                url = 'https://china.guidechem.com' + text
                request = scrapy.Request(url, method='GET', callback=self.parse_s,
                                         encoding='utf-8')
                yield request
                #item['cas'] = text
                #print(cas)
                #yield scrapy.Request(url = u,callback = self.parse_s)
                #yield item
        #/html/body/div[2]/div[4]/div[2]/table/tbody/tr/td[3]/table[4]/tbody/tr/td/a[10]
        next = response.xpath('//table[4]//tr/td/a[10]/@href').extract()[0]
        # item = MsdsItem()
        # item['xiayy'] = next
        ur = response.urljoin(next)
        yield scrapy.Request(url=ur, callback=self.parse)
    
    
    def parse_s(self,response):
        
        item = MsdsItem()
        guoji = response.xpath('//table[@bgcolor="#CADBEF"]//tr[1]/td[2]').extract()[0]
        item['cas'] = guoji                                                                                               
        yield item
        #/html/body/div[2]/div[4]/div[2]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]

        #/html/body/div[2]/div[4]/div[2]/table/tbody/tr/td[3]/table
        
        '''
        item = MsdsItem()
        text = response.xpath('//table[@class="bk"]//tr[1]/td[1]/a/@href').extract()
        item['cas'] = text                                                                                               
        yield item
        
        item = MsdsItem()
        text = response.xpath('//table[4]//tr/td/a[10]/@href').extract()
        item['cas'] = text                                                                                               
        yield item
        '''