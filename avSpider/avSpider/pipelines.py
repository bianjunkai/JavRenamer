# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os, codecs, urllib
from xml.etree.ElementTree import Element, SubElement, ElementTree
from avSpider.traversal import moveFile

class AvspiderPipeline(object):
    # def process_item(self, item, spider):
    #     with codecs.open(os.path.join(os.getcwd() + "metadata.txt"), 'a', encoding='utf-8') as f:
    #         for key in item.keys():
    #             f.write(item.get(key) + "\n")
    #     return item

    def process_item(self, item, spider):
        root = Element('movie')
        WORK_PATH = os.path.dirname(os.getcwd())
        DEST_PATH = os.path.join(WORK_PATH, 'Movies') #Predefined WORD USED
        for key in item.keys():
            if key == 'vid':
                num = SubElement(root, 'num')
                num.text = item.get(key)
            elif key == 'title':
                title = SubElement(root, 'title')
                title.text = item.get(key)
            elif key == 'release_date':
                premiered = SubElement(root, 'premiered')
                premiered.text = item.get(key)
                release = SubElement(root, 'release')
                release.text = item.get(key)
            elif key == 'length':
                runtime = SubElement(root, 'runtime')
                runtime.text = item.get(key)
            elif key == 'director':
                director = SubElement(root, 'director')
                director.text = item.get(key)
            elif key == 'maker':
                maker = SubElement(root, 'maker')
                maker.text = item.get(key)
            elif key == 'label':
                studio = SubElement(root, 'studio')
                label = SubElement(root, 'label')
                studio.text = item.get(key)
                label.text = item.get(key)
            elif key == 'cast':
                actor = SubElement(root, 'actor')
                name = SubElement(actor, 'name')
                name.text = item.get(key)
            elif key == 'rate':
                rating = SubElement(root, 'rating')
                rating.text = item.get(key)
            elif key == 'pic':
                poster = SubElement(root, 'poster')
                thumb = SubElement(root, 'thumb')
                fanart = SubElement(root, 'fanart')
                cover = SubElement(root, 'cover')
                poster.text = item.get(key)
                thumb.text = item.get(key)
                cover.text = item.get(key)
            else:
                pass

        tree = ElementTree(root)
        if item['cast']:
            dictCast = os.path.join(DEST_PATH, item['cast'])
            if not os.path.exists(dictCast):
                os.makedirs(dictCast)
            # tmpName = item['title']
            dictVid = os.path.join(dictCast, item['vid'])
            if not os.path.exists(dictVid):
                os.makedirs(dictVid)
            
            tree.write(os.path.join(dictVid, item['vid'] + '.nfo'), encoding='utf-8')

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
            req = urllib.request.Request(url=item['pic'], headers=headers)
            res = urllib.request.urlopen(req)
            file_name = os.path.join(dictVid, item['vid'] + '.jpg')
            with open(file_name, 'wb') as fp:
                fp.write(res.read())

            fpath = item.get('fpath')
            # print(fpath)
            moveFile(item['vid'],fpath,dictVid)
            print("Move "+item['vid']+"To: "+dictVid+" OK!\n")

        return item
