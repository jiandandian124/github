import time
import scrapy
from msds.items import MsdsItem
import pandas as pd
import json
# scrapy crawl msds03 -o text3.csv
class Msds01Spider(scrapy.Spider):
    name = 'msds03'
    allowed_domains = ['china.guidechem.com']
    start_urls = ['https://china.guidechem.com/datacenter/msds/c/699.html']
    
    def parse(self, response):
        item = MsdsItem()
        #a = response.xpath('//td[@colspan="2"]').extract()[1]
        #qita = pd.read_html(a)
        # qita = pd.read_html(response.text)
        # qita = json.loads(response.text)
        
        a = response.xpath('//td[@colspan="2"]//font[@size="2"]/text()').extract()
        #item['其他'] = qita
        
        #yield item
        data = response.text
        #data = json.loads(response.text)
        #data = pd.read_html(response.text)

        item['其他'] = a
        
        yield item
