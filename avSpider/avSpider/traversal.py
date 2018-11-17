#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, codecs, re, shutil

PATTERN = re.compile(r'[a-zA-Z]{2,4}-?\d{1,4}')

def regLabelAndSerial(vid):
    label = re.findall(r'[a-zA-Z]{2,4}', vid)
    serial = re.findall(r'[0-9]{1,4}', vid)
    index = label[0].upper() + "-" + serial[0]
    return index

# 建立番号和番号对应视频文件直接的索引，并创建文件名问index.txt的索引文件
def creatPATHdict(workpath):
    pathDict = {}
    for fpath, dirs, fs in os.walk(workpath):
        for f in fs:
            if os.path.splitext(f)[1] == ".mp4" or os.path.splitext(f)[1] == ".avi" or os.path.splitext(f)[
                1] == ".mkv":  # verify the video files
                m = re.search(PATTERN, f)
                if m:
                    index = regLabelAndSerial(m.group())
                    pathDict[index] = os.path.join(fpath, f)
    return pathDict

# 找到目标nfo文件的具体位置
def loadDestination(dest_path):
    pathDict = {}
    for fpath, dirs, fs in os.walk(dest_path):
        for f in fs:
            if os.path.splitext(f)[1] == ".nfo":  # verify the video files
                name = os.path.splitext(f)[0]
                pathDict[name] = fpath
    return pathDict

# 搜索和确认仍然未移动的文件
def checkDict(dictname):
    print("CHECK CHECK CHECK:\n")
    for fpath, dirs, fs in os.walk(dictname):  # traversal all videos files in the current dir
        for f in fs:
            if os.path.splitext(f)[1] == ".mp4" or os.path.splitext(f)[1] == ".avi" or os.path.splitext(f)[
                1] == ".mkv":  # verify the video files
                with codecs.open("unmoved.txt", 'w', encoding='utf-8') as fileobject:
                    fileobject.write(os.path.join(fpath, f) + "\n")

# 根据索引移动所有有nfo文件的目标
def moveFiles(orgin_path,dest_path):
    destDict = loadDestination(dest_path)
    originDict = creatPATHdict(orgin_path)
    for index in originDict:
        origin = originDict[index]
        filetype = os.path.splitext(origin)[1]
        filename = index+filetype
        # print(origin)
        if index in destDict.keys():
            destdir = destDict[index]
            destfile = os.path.join(destdir,filename)
            # print("Move to:"+destfile+"\n")
            shutil.move(origin, destfile)
        else:
            continue
    checkDict(orgin_path)

def moveFile(index,origin,dest_path):
    #rename video file
    filetype = os.path.splitext(origin)[1]
    filename = index+filetype
    destfile = os.path.join(dest_path,filename)
    shutil.move(origin,destfile)