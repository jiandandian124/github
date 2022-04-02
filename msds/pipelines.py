# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class MsdsPipeline:
    
    def __init__(self):
        #连接数据库
        self.client = pymongo.MongoClient('localhost')
        #创建库
        self.db = self.client['msds']
        #创建表
        self.table = self.db['msds']

    def process_item(self,item,spider):
        
        self.table.insert(dict(item))
        return item