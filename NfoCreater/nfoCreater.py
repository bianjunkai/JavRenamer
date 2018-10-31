#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: junkai
@file: nfoCreater.py.py
@time: 2018/10/29 0029 下午 7:54
@desc:
'''

from xml.etree.ElementTree import Element, SubElement, ElementTree


def createNfoTree():
    root = Element('movie')
    title = SubElement(root, 'title')
    studio = SubElement(root, 'studio')
    premiered = SubElement(root, 'premiered')
    outline = SubElement(root, 'outline')
    runtime = SubElement(root, 'runtime')
    director = SubElement(root, 'director')
    poster = SubElement(root, 'poster')
    thumb = SubElement(root, 'thumb')
    fanart = SubElement(root, 'fanart')
    actor = SubElement(root, 'actor')
    name = SubElement(actor, 'name')
    maker = SubElement(root, 'maker')
    label = SubElement(root, 'label')
    num = SubElement(root, 'num')
    release = SubElement(root, 'release')
    cover = SubElement(root, 'cover')

    tree = ElementTree(root)
    return tree
