#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,shutil
nowPath = os.getcwd() # get the current dir
tmpVideo = os.path.join(nowPath,"tmpVideo") # create a new dir to store all the video files
for  fpath,dirs,fs in os.walk(nowPath):  # traversal all videos files in the current dir 
    for f in fs:
        if os.path.splitext(f)[1]==".mp4": # verify the video files
            print(os.path.join(fpath,f))
            videFile = os.path.join(fpath,f) # get the full path of video files 
            if not os.path.exists(tmpVideo):
                os.makedirs(tmpVideo) 
            shutil.copy(videFile,tmpVideo) # copy files use shutil.move() to move the file

