#coding:utf-8
from __future__ import absolute_import
import scrapy
import requests
from bs4 import BeautifulSoup
import lxml.etree
import lxml.html as html
from lyrics.items import LyricsItem

gender = 0
f = open('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/song_list.txt','w')
how_many_songs = 0

class wang(scrapy.Spider):
    name = 'wang'

    
    def start_requests(self):
        start_urls=['https://mojim.com/twza1.htm','https://mojim.com/twzb1.htm','https://mojim.com/twzc1.htm']
        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.parse_getgroup)


    def parse_getgroup(self,response):
        global gender
        gender += 1
        print '############'
        count=1
        min=2
        max=32
        if gender == 3 :
            min=28
            max=33
        elif gender == 2:
            max=31
        for i in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s_list", " " ))]//li//a'):
            if count >= min and count <= max:
                url = str(i.xpath('@href').extract()[0])
                url = 'https://mojim.com'+url
                print '____________'
                print url
                print count
                yield scrapy.Request(url=url, callback=self.parse_getperson)
            count+=1
        print '============'

    def parse_getperson(self,response):
        for i in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s_listA", " " ))]//li//a'):
            url = str(i.xpath('@href').extract()[0])
            url = url[0:len(url) - 4]
            url = 'https://mojim.com'+url+'-A1.htm'
            yield scrapy.Request(url=url, callback=self.parse_getsong)

    def parse_getsong(self,response):
        global how_many_songs
        singer = ''.join(response.xpath(u'//*[@id="Tb3"]/a[3]/text()').extract()).encode('utf-8')
        first = 1
        last = ''
        for i in response.selector.xpath(u'//*[contains(concat( " ", @class, " " ), concat( " ", "ha0", " " ))]//dd')[3:]:
            this = "".join(i.xpath('span[2]/a[1]/text()').extract()).encode('utf-8')
            no = "".join(i.xpath('span[2]/a[2]/font').extract()).encode('utf-8')
            year = ("".join(i.xpath('span[5]/text()').extract()))[0:4]
            if this != "" and (not no) and len(year)==4 :
                year = int(year)
                if year >= 2003:
                    print this
                    print year
                    if first:
                        how_many_songs+=1
                        last = this
                        first-=1
                        f.write(str(how_many_songs)+','+this+','+singer+','+'\n')
                        url = 'https://mojim.com'+str(i.xpath('span[2]/a[1]/@href').extract()[0])
                        print url
                        item = LyricsItem()
                        item['number'] = str(how_many_songs)
                        request = scrapy.Request(url=url,callback=self.parse_getlyrics)
                        request.meta['item'] = item
                        yield request
                    else:
                        if(last==this):
                            continue
                        else:
                            last = this
                            how_many_songs+=1
                            f.write(str(how_many_songs)+','+this+','+singer+','+'\n')
                            url = 'https://mojim.com'+str(i.xpath('span[2]/a[1]/@href').extract()[0])
                            print url
                            item = LyricsItem()
                            item['number'] = str(how_many_songs)
                            request = scrapy.Request(url=url,callback=self.parse_getlyrics)
                            request.meta['item'] = item
                            yield request

    def parse_getlyrics(self,response):
        item = response.meta['item']
        print response
        c_list = "".join(response.selector.xpath('//*[@id="fsZx3"]').extract())
        doc = html.document_fromstring(c_list)
        for i in doc.xpath("*//br"):
            i.tail = "\n"+i.tail if i.tail else "\n"
            s = i.tail.encode('utf-8')
        print doc.text_content().encode('utf-8')
        item['content'] = doc.text_content().encode('utf-8')
        yield item

#'//*[@id="Tb3"]/table[2]/tbody[1]/tr[2]/td[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/dl[2]/dd[1]'

#        for i in c_list:
#        t="".join(c_list.xpath('text()').extract()).encode('utf-8')
#        print t

#|//*[@id="Tb3"]/table[2]/tbody[1]/tr[2]/td[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/dl[2]/dd//br

"""
        if t:
            if t[0]=='[':
                break;
        if t.find('更多更詳盡歌詞') | t.find('：') :
            continue;
        if t.find('<br>'):
            t=''
        content+='\n'
        item['content'] = content
        yield item
"""

'''
    def parse(self,response):
        item = AliItem()
        soup = BeautifulSoup(response.body,'lxml')
        for i in soup.find_all('dd',id='fsZx3'):
            item['content'] = i.get_text()
            yield item
'''
