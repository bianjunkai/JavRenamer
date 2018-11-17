#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: junkai
@file: run.py
@time: 2018/11/12 0027 下午 10:36
@desc: main functions
'''

import os,re
from Traversal import traversal
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

WORK_PATH =  os.getcwd()
ORIN_PATH = os.path.join(WORK_PATH,"unmoved") 
DEST_PATH = os.path.join(WORK_PATH,"Movies")

# 获得unmoved文件夹中所有的番号和番号对应视频文件及关联索引
traversal.creatPATHdict(ORIN_PATH)

process = CrawlerProcess(get_project_settings())
process.crawl('w24spider')
process.start()

traversal.moveFiles(ORIN_PATH,DEST_PATH)


