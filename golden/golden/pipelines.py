# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class GoldenPipeline(object):
    root_path = 'F:\\广西卫建委\\'
    def process_item(self, item, spider):
        path = self.root_path + item['path']
        if (not os.path.exists(path)):
            os.makedirs(path)
        filename = item['title'].replace(':', '') + '.txt'
        fp = open(path + '/' + filename, 'w', encoding='utf-8')
        fp.write('<<<原文链接：' + item['infoUrl'] + '>>>' + '\n\n     ' +
                      item['info'] + '\n\n' +
                   '<<<附件下载地址：' + item['docUrlPath'] + '>>>\n' + item['source'])
        fp.close()
        return item

