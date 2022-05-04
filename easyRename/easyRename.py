#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: junkai
@file: easyReanme.py
@time: 2022/5/3 0001 下午 10:23
@desc: 目的对所有下载的迅雷影片，进行一次重命名。分为两步，1.找到文件，获取文件名 2. 解析文件名称，并标准化文件名属性
''' 
import os, codecs, re, shutil

def find_file():
    nowPath = os.getcwd() # get the current dir
    for fpath,dirs,fs in os.walk(nowPath):  # traversal all videos files in the current dir 
        for f in fs:
            if os.path.splitext(f)[1] == ".mp4" or os.path.splitext(f)[1] == ".avi" or os.path.splitext(f)[
                1] == ".mkv":  # verify the video files
                video_File = os.path.join(fpath,f)
                print(video_File)
                namefile = name_of_file(video_File)
                print(namefile)
                if name_check(video_File,namefile):
                    print(namefile)
                    new_video_File = os.path.join(fpath,namefile)
                    print(new_video_File)
                    os.rename(video_File,new_video_File)
                else:
                    continue

def name_of_file(video_File):
    path_file = os.path.split(video_File)[0]
    name_of_file = os.path.split(video_File)[1]
    filetype = os.path.splitext(video_File)[1]
    pattern = re.compile(r'[a-zA-Z]{2,5}-?\d{1,4}')
    m = re.search(pattern, name_of_file)
    if m:
        if with_sub(name_of_file):
            newfile = os.path.join(path_file,m.group()+"-C"+filetype)
        else:
            newfile = os.path.join(path_file,m.group()+filetype)
        return newfile
    else :
        return 0

def  with_sub(name_of_file):
    pattern = re.compile(r'[a-zA-Z]{2,4}-?\d{2,4}[-_]?[Cc][hH]?')
    m = re.search(pattern, name_of_file)
    if m:
        return True

def name_check(video_File,name_of_file):
    return True if video_File != name_of_file else False

if __name__=="__main__":
    find_file()