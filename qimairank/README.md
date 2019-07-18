# Scrapy 爬取七麦 app数据排行榜
熟悉Scrapy之后，本篇文章带大家爬取七麦数据（https://www.qimai.cn/rank ）的ios appstore付费应用排行榜前100名应用。

爬取内容包括app在列表中的下标，app图标地址，app的名称信息，app的类型，在分类中的排行，开发者，详情等。

考虑的问题：
+ Forbidden by robots.txt的错误
+ 网页返回403
+ 页面通过动态渲染，普通的请求url，在页面渲染之前已经返回response，解析没有数据
+ 列表一页20个app，想要拿到前100个需要翻页，但是翻页没有更改url，而是通过js动态加载
+ ...

[详情查看](https://luohongxfb.github.io/2019/07/16/Scrapy-爬取七麦-app数据排行榜/)