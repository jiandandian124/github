from pymongo import MongoClient
from pymongo import InsertOne
import time

def insert():
    #连接数据库
    conn = MongoClient('localhost',maxPoolSize=None)
    my_db = conn['msds']
    my_collection = my_db['urls']

    data = []
    for i in range(699,10985):
        ne = 'https://china.guidechem.com/datacenter/msds/c/%d.html'%(i)
        data.append(InsertOne({"id":i, "url":ne,"state":"1"}))
    my_collection.bulk_write(data)
    # 批量写
    # i = 0
    # t0 = time.time()
    # data =[]
    # while True:
    #     #'_id'为主键，循环时递增，全部添加到data列表内
    #     data.append(InsertOne({"_id":i,"insert_time": int(time.time() * 1000)}))
    #     i+=1
    #     #判断列表长度，达到10000执行插入，后继续循环
    #     if len(data) == 10000:
    #         my_collection.bulk_write(data)
    #         res = []
    #         i += 1
    #         continue
    #   #判断i等于1亿时停止循环
    #     elif i == 100000000:
    #          break

if __name__ == '__main__':
    insert()
    print('写入成功！')


# class TongjiPipeline:
# def __init__(self):
#         # self.client = MongoClient(settings.DATA_MONGODB_URI)
#         # self.db = self.client[settings.DATA_MONGODB_DBNAME]
#         #连接数据库
#         self.client = pymongo.MongoClient('localhost')
#         #创建库
#         self.db = self.client['msds']
#         #创建表
#         self.table = self.db['urls']


#         for i in range(699,10985):
#             ne = 'https://china.guidechem.com/datacenter/msds/c/%d.html'%(i)
#             result = 
#         print(result)
#         return
