import scrapy
from demjson import JSON
from scrapy import Request

from qimairank.items import RankItem


class RankSpider(scrapy.Spider):
    name = "RankSpider"
    start_urls = ["https://www.qimai.cn/rank"]

    # def start_requests(self):
    #     yield Request(self.start_urls[0], self.parse, meta={'count': 0},
    #                   dont_filter=True)

    def parse(self, response):
        # print(response.xpath("//body").extract())
        base = response.xpath(
            "//div[@class='ivu-row rank-all-item']/div[@class='ivu-col ivu-col-span-8'][2]//ul/li[@class='child-item']/div[@class='ivu-row']")
        for box in base:
            # 创建实例
            rankItem = RankItem()
            # 下标
            rankItem['index'] = \
                box.xpath(".//div[@class='ivu-col ivu-col-span-3 left-item']/span/text()").extract()[0]
            if int(rankItem['index']) <= 100:
                # 图标地址
                rankItem['src'] = box.xpath(".//img/@src").extract()[0]
                # app名称信息
                rankItem['title'] = box.xpath(".//div[@class='info-content']//a/text()").extract()[0]
                # app类型
                rankItem['type'] = box.xpath(".//div[@class='info-content']//p[@class='small-txt']/text()").extract()[0]
                # 分类中的排行
                rankItem['type_rank'] = box.xpath(
                    ".//div[@class='info-content']//p[@class='small-txt']//span[@class='rank-item']/text()").extract()[
                    0]
                # 开发者
                rankItem['company'] = box.xpath(
                    ".//div[@class='info-content']//p[@class='small-txt']//span[@class='company-item']/text()").extract()[
                    0]
                # 详情页地址
                infoUrl = "https://www.qimai.cn" + box.xpath(".//div[@class='info-content']//a/@href").extract()[0]
                # yield rankItem
                yield Request(infoUrl.replace("rank", "baseinfo"), self.parseInfo,
                              meta={'rankItem': dict(rankItem).copy()}, dont_filter=True)

    def parseInfo(self, response):
        print("基地址：" + response.url)
        if response.status != 200:
            return

        rankItem = response.meta['rankItem']

        info = dict()
        base = response.xpath("//div[@id='app-container']")
        if base.extract():
            # try:
            # 描述
            try:
                info['desc'] = base.xpath(
                    ".//div[@class='app-header']//div[@class='app-subtitle']/text()").extract()[0]
            except Exception as e:
                print("无描述")
            # 开发商
            info['auther'] = base.xpath(
                ".//div[@class='app-header']//div[@class='auther']//div[@class='value']/text()").extract()[0]
            # 分类
            info['classify'] = base.xpath(
                ".//div[@class='app-header']//div[@class='genre']//div[@class='value']/a/text()").extract()[0]
            # appid
            info['appid'] = base.xpath(
                ".//div[@class='app-header']//div[@class='appid']//div[@class='value']/a/text()").extract()[0]
            # appstore地址
            info['appstorelink'] = base.xpath(
                ".//div[@class='app-header']//div[@class='appid']//div[@class='value']/a/@href").extract()[0]
            # 价格
            info['price'] = base.xpath(
                ".//div[@class='app-header']//div[@class='price']//div[@class='value']/text()").extract()[0]
            # 最新版本
            info['version'] = base.xpath(
                ".//div[@class='app-header']//div[@class='version']//div[@class='value']/text()").extract()[0]
            # 应用截图
            info['screenshot'] = base.xpath(
                ".//div[@class='router-wrapper']//div[@class='app-screenshot']//div[@class='screenshot-box']//img/@src").extract()
            # 应用描述
            info['desc'] = base.xpath(
                ".//div[@class='router-wrapper']//div[@class='app-describe']//div[@class='description']").extract()[
                0]
            # 应用基本信息
            info['baseinfo'] = []
            for infoBase in base.xpath(
                    ".//div[@class='router-wrapper']//div[@class='app-baseinfo']//ul[@class='baseinfo-list']/li"):
                # print(info['baseinfo'])
                try:
                    info['baseinfo'].append(dict(type=infoBase.xpath(".//*[@class='type']/text()").extract()[0],
                                                 info=infoBase.xpath(".//*[@class='info-txt']/text()").extract()[0]))
                except Exception as e:
                    pass

            rankItem['info'] = info
            # 替换图标 列表加载为默认图标
            rankItem['src'] = \
                response.xpath("//*[@id='app-side-bar']//div[@class='logo-wrap']/img/@src").extract()[
                    0]
            yield rankItem
            # print(rankItem)
            # except Exception as e:
            #     print(response.url + " 解析报错")
            #     print(e)
