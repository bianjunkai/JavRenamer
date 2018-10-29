# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os, codecs


class AvspiderPipeline(object):
    def process_item(self, item, spider):
        with codecs.open(os.path.join(os.getcwd() + "metadata.txt"), 'a', encoding='utf-8') as f:
            for key in item.keys():
                f.write(item.get(key) + "\n")
        return item
