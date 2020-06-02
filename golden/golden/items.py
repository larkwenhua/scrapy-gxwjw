# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoldenItem(scrapy.Item):
    # define the fields for your item here like:

    """
    title = scrapy.Field()   # 文件名称
    path = scrapy.Field()    # 文件路径
    source = scrapy.Field()  # 文件来源
    info = scrapy.Field()    # 文件内容
    infoUrl = scrapy.Field()    # 文件内容链接
    docUrlPath = scrapy.Field()    # 下载文件链接
    """
    name = scrapy.Field()    # 机构名称
    index = scrapy.Field()   # 索引号
    title = scrapy.Field()   # 标题
    content = scrapy.Field()    # 内容
    release = scrapy.Field()  # 发布机构
    time = scrapy.Field()    # 发布时间
    number = scrapy.Field()    # 文号
