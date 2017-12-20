# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import absolute_import
from scrapy import signals
import json
import codecs
from lyrics.items import LyricsItem


class LyricsPipeline(object):
    def process_item(self, item, spider):
        print '------pipelines------'
        f = open('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/lyrics/'+item['number']+'.txt','w')
        f.write(item['content'])
        f.close()
        return item
