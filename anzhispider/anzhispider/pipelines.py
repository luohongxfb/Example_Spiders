# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

import os

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline

from anzhispider.settings import FILES_STORE
from anzhispider.utils.MySQLHelper import MySQLHelper
from anzhispider.utils import parseProperty, parseImageList


class AnzhispiderPipeline(object):
    """
    数据库存储
    """

    def __init__(self):
        # 打开数据库链接
        self.mysqlHelper = MySQLHelper()

    def process_item(self, item, spider):
        # 数据库存储的sql
        sql = "INSERT INTO games(link,name,versionCode,icon,type,onlineTime,size,download,author,intro,updateInfo,highlight,image1,image2,image3,image4,image5) " \
              "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                  item['link'], item['name'], parseProperty(item, "versionCode", "v1.0"),
                  parseProperty(item, "iconPath", ""), parseProperty(item, "type", ""),
                  parseProperty(item, "onlineTime", ""), parseProperty(item, "size", "0B"),
                  parseProperty(item, "download", "0"), parseProperty(item, "author", "未知"),
                  parseProperty(item, "intro", "无"), parseProperty(item, "updateInfo", "无"),
                  parseProperty(item, "highlight", "无"), parseImageList(item, 0), parseImageList(item, 1),
                  parseImageList(item, 2), parseImageList(item, 3), parseImageList(item, 4))
        # 插入数据
        self.mysqlHelper.update(sql)
        return item


class ImageResPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        '''
        根据文件的url发送请求（url跟进）
        :param item:
        :param info:
        :return:
        '''
        # 根据index区分是icon图片还是市场图
        yield scrapy.Request(url='http://www.anzhi.com' + item['icon'], meta={'item': item, 'index': 0})
        # 市场图下载
        for i in range(0, len(item['images'])):
            yield scrapy.Request(url='http://www.anzhi.com' + item['images'][i], meta={'item': item, 'index': (i + 1)})

    def file_path(self, request, response=None, info=None):
        '''
        自定义文件保存路径
        默认的保存路径是在FILES_STORE下创建的一个full来存放，如果我们想要直接在FILES_STORE下存放或者日期路径，则需要自定义存放路径。
        默认下载的是无后缀的文件，根据index区分，icon需要增加.png后缀，市场图增加.jpg后缀
        :param request:
        :param response:
        :param info:
        :return:
        '''
        item = request.meta['item']
        index = request.meta['index']
        today = str(datetime.date.today())
        # 定义在FILES_STORE下的存放路径为YYYY/MM/dd/app名称，如2019/11/28/和平精英
        outDir = today[0:4] + r"\\" + today[5:7] + r"\\" + today[8:] + r"\\" + item['name'] + r"\\"
        if index > 0:
            # index>0为市场图 命名为[index].jpg  注意：以数字命名的文件要转换成字符串，否则下载失败，不会报具体原因！！！
            file_name = outDir + str(index) + ".jpg"
        else:
            # index==0为icon下载，需采用png格式合适
            file_name = outDir + "icon.png"
        # 输出的文件已存在就删除
        if os.path.exists(FILES_STORE + outDir) and os.path.exists(FILES_STORE + file_name):
            os.remove(FILES_STORE + file_name)
        return file_name

    def item_completed(self, results, item, info):
        '''
        处理请求结果
        :param results:
        :param item:
        :param info:
        :return:
        '''
        '''
        results的格式为：
        [(True,
            {'checksum': '2b00042f7481c7b056c4b410d28f33cf',
            'path': 'full/7d97e98f8af710c7e7fe703abc8f639e0ee507c4.jpg',
            'url': 'http://www.example.com/images/product1.jpg'}),
        (True,
            {'checksum': 'b9628c4ab9b595f72f280b90c4fd093d',
            'path': 'full/1ca5879492b8fd606df1964ea3c1e2f4520f076f.jpg',
            'url': 'http://www.example.com/images/product2.jpg'}),
        (False,
            Failure(...))
        ]
        '''
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")

        for file_path in file_paths:
            if file_path.endswith("png"):
                # icon的图片地址赋值给iconPath
                item['iconPath'] = FILES_STORE + file_path
            else:
                # 市场图的地址给imagePaths 不存在属性就创建空数组
                if 'imagePaths' not in item:
                    item['imagePaths'] = []
                item['imagePaths'].append(FILES_STORE + file_path)
        return item
