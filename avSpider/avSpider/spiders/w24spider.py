# -*- coding: utf-8 -*-
import scrapy
import os, re
import urllib
from avSpider.items import AvspiderItem


class W24spiderSpider(scrapy.Spider):
    name = 'w24spider'
    allowed_domains = ['www.w24j.com']
    start_urls = ['http://www.w24j.com/cn/']
    vidsets = set()

    def parse(self, response):
        indexFile = os.path.join(os.getcwd(), "index.txt")
        with open(indexFile, 'r') as f:
            for onevid in f.readlines():
                W24spiderSpider.vidsets.add(onevid)
        for vid in W24spiderSpider.vidsets:
            url = 'http://www.w24j.com/cn/vl_searchbyid.php?keyword=' + vid.strip()
            yield scrapy.Request(url, callback=self.parse_movie)

    pass

    def parse_movie(self, response):
        title = response.xpath("//*[@id=\"video_title\"]/h3/a/text()")
        item = AvspiderItem()
        vid = response.xpath("//*[@id=\"video_id\"]//td[@class=\"text\"]/text()")
        date = response.xpath("//*[@id=\"video_date\"]//td[@class=\"text\"]/text()")
        # vid = re.search("[a-zA-Z]{2,5}-?d{2,5}", title).group(0)
        print(vid)
        name = title[len(vid) + 1:]
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
        if name:
            item["title"] = name.extract()[0]
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
