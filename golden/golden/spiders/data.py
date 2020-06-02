# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging
from lxml import etree

class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['wsjkw.gxzf.gov.cn']
    start_urls = [
                  # 'http://wsjkw.gxzf.gov.cn/',
                  # 'http://wsjkw.gxzf.gov.cn/gzdt/gs/2020/0528/72734.html',  不含文件
                  # 'http://wsjkw.gxzf.gov.cn/xzzc/2020/0207/68536.html'  含文件
                    'http://wsjkw.gxzf.gov.cn/zwgk/zfxxgkml/'     # 领导分工信息
                  ]

    # 提取详情页URL
    link = LinkExtractor( allow=[
                r'zwgk/zfxxgkml'
                          ])
    links = LinkExtractor(restrict_xpaths="//*[contains(@class, 'node')]/@href|//*[contains(@class, 'a1')]/@href")  # 不传入任何参数，就会自动提取页面中的所有的链接
    linka = LinkExtractor()

    rules = (
        # Rule(link, callback='parse_item', follow=True),
        Rule(link, callback='parse_jgzn', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = {}
        title = response.xpath('//div[2]/h1/text()').extract()
        if title:
            item['title'] = title[0]
            item['path'] = '/'.join(response.xpath('/html/body/div[3]/div[1]/a/text()').extract())
            item['source'] = response.xpath('//span/div[1]/text()').extract()[0].replace('\xa0\xa0', ' ')
            item['info'] = ''.join(response.xpath('//div[5]/p//text()').extract())
            item['docUrlPath'] = ''.join(response.xpath('//div/p//a/@href').extract())
            item['infoUrl'] = response.url
            logging.info('正在解析的地址：'+response.url)
            return item

    def parse_jgzn(self, response):
        item = {}
        print(response.url+'*******************')

        index = ''.join(response.xpath('/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr/td[1]/text()').extract())
        if response.xpath('//*[@id="ListName"]/text()').extract() and index == '索引号':

            item['name'] = ''.join(response.xpath('//*[@id="ListName"]/text()').extract())
            index = response.xpath('/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr/td[1]').extract()
            titleList = response.xpath('/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr/td[2]').extract()
            contentList = response.xpath('/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr/td[3]').extract()
            releaseList = response.xpath('/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr/td[4]').extract()
            timeList = response.xpath('/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr/td[5]').extract()
            numberList = response.xpath('/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr/td[6]').extract()

            for a, b, c, d, e, f in zip(titleList, contentList, releaseList, timeList, numberList, index):
                diva = etree.HTML(a)
                item['title'] = ''.join(diva.xpath('//text()'))
                divb = etree.HTML(b)
                item['content'] = ''.join(divb.xpath('//text()'))
                divc = etree.HTML(c)
                item['release'] = ''.join(divc.xpath('//text()'))
                divd = etree.HTML(d)
                item['time'] = ''.join(divd.xpath('//text()'))
                dive = etree.HTML(e)
                item['number'] = ''.join(dive.xpath('//text()'))
                divf = etree.HTML(f)
                item['index'] = ''.join(divf.xpath('//text()'))
                yield item


