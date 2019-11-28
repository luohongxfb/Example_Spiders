import json

from scrapy import Spider

from anzhispider.items import AnzhispiderItem


class AnzhiSpider(Spider):
    name = "AnzhiSpider"
    # 允许访问的域
    allowed_domains = ["www.anzhi.com"]

    start_urls = ["http://www.anzhi.com/pkg/3d81_com.tencent.tmgp.pubgmhd.html"]

    # start_urls = ["http://www.anzhi.com/pkg/3d81_com.tencent.tmgp.pubgmhd.html","http://www.anzhi.com/pkg/84bf_com.sxiaoao.feijidazhan.html","http://www.anzhi.com/pkg/4f41_com.tencent.tmgp.WePop.html"]

    def parse(self, response):
        item = AnzhispiderItem()
        root = response.xpath('.//div[@class="content_left"]')
        # 链接
        item['link'] = response.url
        # 图标
        item['icon'] = root.xpath('.//div[@class="app_detail"]/div[@class="detail_icon"]/img/@src').extract()[0]
        # app名称
        item['name'] = root.xpath(
            './/div[@class="app_detail"]/div[@class="detail_description"]/div[@class="detail_line"]/h3/text()').extract()[
            0]
        # 版本号
        item['versionCode'] = root.xpath(
            './/div[@class="app_detail"]/div[@class="detail_description"]/div[@class="detail_line"]/span[@class="app_detail_version"]/text()').extract()[
            0]
        if item['versionCode'] and item['versionCode'].startswith("(") and item['versionCode'].endswith(")"):
            item['versionCode'] = item['versionCode'][1:-1]

        # 分类、上线时间、大小、下载量、作者  先获取所有的详情
        details = root.xpath(
            './/div[@class="app_detail"]/div[@class="detail_description"]/ul[@id="detail_line_ul"]/li/text()').extract()
        details_right = root.xpath(
            './/div[@class="app_detail"]/div[@class="detail_description"]/ul[@id="detail_line_ul"]/li/span/text()').extract()
        details.extend(details_right)

        for detailItem in details:
            if detailItem.startswith("分类："):
                item['type'] = detailItem[3:]
                continue
            if detailItem.startswith("时间："):
                item['onlineTime'] = detailItem[3:]
                continue
            if detailItem.startswith("大小："):
                item['size'] = detailItem[3:]
                continue
            if detailItem.startswith("下载："):
                item['download'] = detailItem[3:]
                continue
            if detailItem.startswith("作者："):
                item['author'] = detailItem[3:]
                continue

        # 简介
        item['intro'] = root.xpath(
            './/div[@class="app_detail_list"][contains(./div[@class="app_detail_title"],"简介")]/div[@class="app_detail_infor"]').extract()
        if item['intro']:
            item['intro'] = item['intro'][0].replace('\t', '').replace('\n', '').replace('\r', '')
        else:
            item['intro'] = ""
        # 更新说明
        item['updateInfo'] = root.xpath(
            './/div[@class="app_detail_list"][contains(./div[@class="app_detail_title"],"更新说明")]/div[@class="app_detail_infor"]').extract()
        if item['updateInfo']:
            item['updateInfo'] = item['updateInfo'][0].replace('\t', '').replace('\n', '').replace('\r', '')
        else:
            item['updateInfo'] = ""
        # 精彩内容
        item['highlight'] = root.xpath(
            './/div[@class="app_detail_list"][contains(./div[@class="app_detail_title"],"精彩内容")]/div[@class="app_detail_infor"]').extract()
        if item['highlight']:
            item['highlight'] = item['highlight'][0].replace('\t', '').replace('\n', '').replace('\r', '')
        else:
            item['highlight'] = ""

        # 市场图地址
        item['images'] = root.xpath(
            './/div[@class="app_detail_list"][contains(./div[@class="app_detail_title"],"软件截图")]//ul/li/img/@src').extract()
        yield item
