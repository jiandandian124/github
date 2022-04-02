import scrapy
import json
import pandas as pd
import numpy as np
# scrapy crawl demo -o demo.csv
class IpSpiderSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['www.ip.cn']
    start_urls = ['https://www.ip.cn/']

    def parse(self, response):
        origin = pd.read_html(response.text)
        #origin = json.loads(response.body)
        # origin = response.xpath('//*[@id="tab0_ip"]/text()').extract()
        m = np.array(origin)
        np.save('demo.npy',m)
        a=np.load('demo.npy',allow_pickle=True)
        demo=a.tolist()
        print('1111'*20)
        print(origin)
        print('2222'*20)
        print(demo)
        print('3333'*20)

        # yield scrapy.Request(self.start_urls[0],dont_filter=True)
