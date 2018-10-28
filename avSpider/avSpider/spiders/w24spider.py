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
        title = response.xpath("//*[@id=\"video_title\"]/h3/a/text()").extract()[0]
        item = AvspiderItem()
        vid = response.xpath("//*[@id=\"video_id\"]//td[@class=\"text\"]/text()").extract()[0]
        date = response.xpath("//*[@id=\"video_date\"]//td[@class=\"text\"]/text()").extract()[0]
        # vid = re.search("[a-zA-Z]{2,5}-?d{2,5}", title).group(0)
        print(vid)
        name = title[len(vid) + 1:]
        pic = "http:" + response.xpath("//*[@id=\"video_jacket_img\"]/@src").extract()[0]
        length = response.xpath("//*[@id=\"video_length\"]//span[@class=\"text\"]/text()").extract()[0]
        director = response.xpath("//*[@id=\"video_director\"]//span[@class=\"director\"]/a/text()").extract()[0]
        maker = response.xpath("//*[@id=\"video_maker\"]//span[@class=\"maker\"]/a/text()").extract()[0]
        label = response.xpath("//*[@id=\"video_label\"]//span[@class=\"label\"]/a/text()").extract()[0]
        cast = response.xpath("//*[@id=\"video_cast\"]//span[@class=\"star\"]/a/text()").extract()[0]
        # item["url"] = response.url
        item["vid"] = vid
        item["title"] = name
        item["pic"] = pic
        item["release_date"] = date
        item["length"] = length
        item["director"] = director
        item["maker"] = maker
        item["label"] = label
        item["cast"] = cast
        yield item
