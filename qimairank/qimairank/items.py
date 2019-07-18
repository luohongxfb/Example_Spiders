# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QimairankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class RankItem(scrapy.Item):
    # 下标
    index = scrapy.Field()
    # 图标地址
    src = scrapy.Field()
    # app标题信息
    title = scrapy.Field()
    # app类型
    type = scrapy.Field()
    # 分类中的排行
    type_rank = scrapy.Field()
    # 公司
    company = scrapy.Field()
    # 详情
    info = scrapy.Field()
