# -*- coding: utf-8 -*-
import scrapy
import os, re
import urllib
import sys
sys.path.append("..")
from avSpider.traversal import creatPATHdict,regLabelAndSerial,checkDict
from avSpider.items import AvspiderItem


class W24spiderSpider(scrapy.Spider):
    name = 'w24spider'
    allowed_domains = ['www.w24j.com']
    start_urls = ['https://www.w24j.com/cn/']  
    
    def parse(self, response):
        WORK_PATH = os.path.dirname(os.getcwd())
        ORIN_PATH = os.path.join(WORK_PATH,"unmoved") 
        DEST_PATH = os.path.join(WORK_PATH,"Movies")
        videos = creatPATHdict(ORIN_PATH)
        vidsets = set()
        # print(videos)
        for onevid in videos.keys():
            vidsets.add(onevid)
        # indexFile = os.path.join(os.getcwd(), "index.txt")  #Predefined WORD USED
        # with open(indexFile, 'r') as f:
        #     for onevid in f.readlines():
        #         
        for vid in vidsets:
            # print(vid)
            url = 'https://www.w24j.com/cn/vl_searchbyid.php?keyword=' + vid.strip()
            # print(videos)
            fpath = videos.get(vid)
            # print(fpath)
            yield scrapy.Request(url,meta={'fpath':fpath},callback=self.parse_movie)
        checkDict(ORIN_PATH)
    pass

    def parse_movie(self, response):    
        fpath = response.meta['fpath']   
        # print(fpath)
        if response.url.startswith("https://www.w24j.com/cn/?v=jav"):
            title = response.xpath("//*[@id=\"video_title\"]/h3/a/text()")
            item = AvspiderItem()
            vid = response.xpath("//*[@id=\"video_id\"]//td[@class=\"text\"]/text()")
            date = response.xpath("//*[@id=\"video_date\"]//td[@class=\"text\"]/text()")
            # vid = re.search("[a-zA-Z]{2,5}-?d{2,5}", title).group(0)
            pic = response.xpath("//*[@id=\"video_jacket_img\"]/@src")
            length = response.xpath("//*[@id=\"video_length\"]//span[@class=\"text\"]/text()")
            director = response.xpath("//*[@id=\"video_director\"]//span[@class=\"director\"]/a/text()")
            maker = response.xpath("//*[@id=\"video_maker\"]//span[@class=\"maker\"]/a/text()")
            label = response.xpath("//*[@id=\"video_label\"]//span[@class=\"label\"]/a/text()")
            cast = response.xpath("//*[@id=\"video_cast\"]//span[@class=\"star\"]/a/text()")
            rate = response.xpath("//*[@id=\"video_review\"]//span[@class=\"score\"]/text()")
            # item["url"] = response.url
            if vid:
                item["vid"] = vid.extract()[0]
                item["fpath"] = fpath
            if title:
                item["title"] = title.extract()[0]
            if pic:
                item["pic"] = "http:" + pic.extract()[0]
            if date:
                item["release_date"] = date.extract()[0]
            if length:
                item["length"] = length.extract()[0]
            if director:
                item["director"] = director.extract()[0]
            if maker:
                item["maker"] = maker.extract()[0]
            if label:
                item["label"] = label.extract()[0]
            if cast:
                item["cast"] = cast.extract()[0]
            if rate:
                item["rate"] = rate.extract()[0]
            yield item
        elif response.url.startswith("https://www.w24j.com/cn/vl_searchbyid.php?keyword="):
            searchkeyword = response.url.split("=")[1]
            vid = regLabelAndSerial(searchkeyword)
            # print(vid)
            for av in response.xpath("//div[@class=\"video\"]/a"):
                href = av.xpath("@href").extract()[0]
                title = av.xpath("@title").extract()[0].split(" ")[0]
                # print(title)
                # print(href)
                if (title == vid):
                    url = urllib.parse.urljoin('https://www.w24j.com/cn/', href)
                    print(url)
                    yield scrapy.Request(url, meta={'fpath':fpath},callback=self.parse_movie)
                    break
        else:
            pass
