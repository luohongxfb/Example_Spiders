# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnzhispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 链接地址
    link = scrapy.Field()
    # app名称
    name = scrapy.Field()
    # 版本号
    versionCode = scrapy.Field()
    # 游戏图标icon
    icon = scrapy.Field()
    # icon存储地址
    iconPath = scrapy.Field()
    # 分类
    type = scrapy.Field()
    # 上线时间
    onlineTime = scrapy.Field()
    # 大小
    size = scrapy.Field()
    # 下载量
    download = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 简介
    intro = scrapy.Field()
    # 更新说明
    updateInfo = scrapy.Field()
    # 精彩内容
    highlight = scrapy.Field()
    # 市场图  字符数组
    images = scrapy.Field()
    # 市场图存储地址
    imagePaths = scrapy.Field()
