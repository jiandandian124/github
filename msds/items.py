# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MsdsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    国标编号 = scrapy.Field()
    CAS = scrapy.Field()
    中文名称 = scrapy.Field()
    英文名称 = scrapy.Field()
    别名 = scrapy.Field()
    分子式 = scrapy.Field()
    分子量 = scrapy.Field()
    熔点 = scrapy.Field()
    密度 = scrapy.Field()
    蒸汽压 = scrapy.Field()
    溶解性 = scrapy.Field()
    稳定性 = scrapy.Field()
    外观与性状 = scrapy.Field()
    危险标记 = scrapy.Field()
    用途 = scrapy.Field()
    其他 = scrapy.Field()
    id = scrapy.Field()
