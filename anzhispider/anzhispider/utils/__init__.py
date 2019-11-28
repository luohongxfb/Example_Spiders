# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
def parseProperty(item, property, defaultValue):
    """
    判断对象的对应属性是否为空 为空就返回默认值
    :param item: 对象
    :param property: 属性名称
    :param defaultValue: 默认值
    """
    if property in item and item[property]:
        return item[property]
    else:
        return defaultValue


def parseImageList(item, index):
    """
    返回市场图地址
    :param item:
    :param index:
    :return:
    """
    if "imagePaths" in item and item["imagePaths"]:
        # 有图片
        # 获取数组大小
        if len(item["imagePaths"]) >= index + 1:
            return item["imagePaths"][index]
        else:
            return ""
    else:
        return ""
