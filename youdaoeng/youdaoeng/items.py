# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoudaoengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 单词
    word = scrapy.Field()
    # 英式发音
    pron = scrapy.Field()
    # 发音audio文件链接
    pron_url = scrapy.Field()
    # 释义
    explain = scrapy.Field()
    # 例句
    example = scrapy.Field()
    # 发音 mp3 本地存放路径
    pron_save_path = scrapy.Field()
