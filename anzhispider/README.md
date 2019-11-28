# Scrapy-爬取安智市场app详情
利用Scrapy扒取安智市场的app详情页，如点击查看[和平精英](http://www.anzhi.com/pkg/3d81_com.tencent.tmgp.pubgmhd.html)，包括app名、版本号、图标icon、分类、时间、大小、下载量、作者、简介、更新说明、软件截图、精彩内容等，扒取的图片资源icon和市场展示图（app截图）下载到本地，并将所有数据存储到数据库。

考虑的问题：
+ 存储的数据库设计
+ 图片资源链接存在重定向
+ 下载app的图标需为.png后缀
+ ...

[详情查看](http://sunflowercoder.com/Scrapy-爬取安智市场app详情/)