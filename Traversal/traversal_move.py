#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: junkai
@file: traversal_move.py.py
@time: 2018/11/1 0001 上午 7:54
@desc:
'''

import os, codecs, re, shutil

WORKPATH = os.getcwd()
DESTINATION_PATH = os.path.join(WORKPATH, "nfo_cast")
PATTERN = re.compile(r'[a-zA-Z]{2,4}-?\d{1,4}')
destDict = {}


def creatPATHdict(dictname):
    pathDict = {}
    for fpath, dirs, fs in os.walk(os.path.join(WORKPATH, dictname)):
        for f in fs:
            if os.path.splitext(f)[1] == ".mp4" or os.path.splitext(f)[1] == ".avi" or os.path.splitext(f)[
                1] == ".mkv":  # verify the video files
                m = re.search(PATTERN, f)
                if m:
                    label = re.findall(r'[a-zA-Z]{2,4}', m.group())
                    serial = re.findall(r'[0-9]{1,4}', m.group())
                    index = label[0].upper() + "-" + serial[0]
                    pathDict[index] = os.path.join(fpath, f)
    return pathDict


def loadDestination():
    pathDict = {}
    for fpath, dirs, fs in os.walk(DESTINATION_PATH):
        for f in fs:
            if os.path.splitext(f)[1] == ".nfo":  # verify the video files
                name = os.path.splitext(f)[0]
                pathDict[name] = fpath
    return pathDict


def checkDict(dictname):
    print("CHECK CHECK CHECK:\n")
    for fpath, dirs, fs in os.walk(dictname):  # traversal all videos files in the current dir
        for f in fs:
            if os.path.splitext(f)[1] == ".mp4" or os.path.splitext(f)[1] == ".avi" or os.path.splitext(f)[
                1] == ".mkv":  # verify the video files
                with codecs.open("unmoved.txt", 'a', encoding='utf-8') as fileobject:
                    fileobject.write(os.path.join(fpath, f) + "\n")


# destDict = loadDestination()
# originDict = creatPATHdict("Movies")
# for index in originDict:
#     origin = originDict[index]
#     filetype = os.path.splitext(origin)[1]
#     filename = index+filetype
#     print(origin)
#     if index in destDict.keys():
#         destdir = destDict[index]
#         destfile = os.path.join(destdir,filename)
#         print("Move to:"+destfile+"\n")
#         shutil.move(origin, destfile)
#     else:
#         continue

checkDict("unmoved")
