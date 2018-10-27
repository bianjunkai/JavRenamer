#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: junkai
@file: cutSerial.py.py
@time: 2018/10/27 0027 下午 9:56
@desc:
'''

import os, re, codecs

currentPath = os.getcwd()
filename = "videoIndex.txt"
newfilename = "index.txt"
# serialDict = ["IPZ", "ONED", "ONSD", "PGD", "JUKD", "JUX", "ATID", "STAR", "ABS","SNIS","DV","DVAJ","SSPD","TKI","CJOD","HND","XRW"]
# regexGroup = []
pattern = re.compile(r'[a-zA-Z]{2,4}-?\d{1,4}')
print(currentPath)
# for serial in serialDict:
#     regex = re.compile(serial+'-?'+'\d{1,3}',re.I)
#     # print(regex)
#     regexGroup.append(regex)

with codecs.open(os.path.join(currentPath, filename), 'r', encoding='utf-8') as f:
    for videoTitle in f.readlines():
        print(videoTitle)
        # for pattern in regexGroup:
        m = re.search(pattern, videoTitle)
        with open(os.path.join(currentPath, newfilename), 'a') as write:
            if m:
                write.write(m.group() + '\n')
            else:
                write.write("NotFound\n")
