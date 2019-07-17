# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
import time
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline

from youdaoeng.settings import FILES_STORE


class YoudaoengPipeline(object):
    def process_item(self, item, spider):
        return item


class Mp3Pipeline(FilesPipeline):
    '''
    自定义文件下载管道
    '''

    def get_media_requests(self, item, info):
        '''
        根据文件的url发送请求（url跟进）
        :param item:
        :param info:
        :return:
        '''
        # meta携带的数据可以在response获取到
        yield scrapy.Request(url=item['pron_url'], meta={'item': item})

    def item_completed(self, results, item, info):
        '''
        处理请求结果
        :param results:
        :param item:
        :param info:
        :return:
        '''
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")

        # old_name = FILES_STORE + file_paths[0]
        # new_name = FILES_STORE + item['word'] + '.mp3'

        # 文件重命名 （相当于剪切）
        # os.rename(old_name, new_name)

        # item['pron_save_path'] = new_name

        # 返回的result是除去FILES_STORE的目录
        item['pron_save_path'] = FILES_STORE + file_paths[0]
        return item

    def file_path(self, request, response=None, info=None):
        '''
        自定义文件保存路径
        默认的保存路径是在FILES_STORE下创建的一个full来存放，如果我们想要直接在FILES_STORE下存放，则需要自定义存放路径。
        默认下载的是无后缀的文件，需要增加.mp3后缀
        :param request:
        :param response:
        :param info:
        :return:
        '''
        file_name = request.meta['item']['word'] + ".mp3"
        return file_name
