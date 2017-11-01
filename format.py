# -*- coding: utf-8 -*-
import jieba
import re

jieba.set_dictionary('/Library/Python/2.6/site-packages/jieba/dict.txt.big.txt')

f=open('/Users/Nini/Desktop/schoolproject/LyricsFile22124/12345.txt','r')
www=open('/Users/Nini/Desktop/schoolproject/LyricsFile22124/s2.txt','w')

data=f.readlines()
www.write('<p> ')
for line in data:
    line = line.replace("　", " ")
    line=line.strip(' ')
    if line[0]=='\n':
        www.write('</p> <p> ')
    elif re.search('[a-zA-z]',line) is not None:
        line = jieba.cut(line)
        line = filter(lambda x: not x.isspace(), line)
        www.write(('<l> <s> ' + u" ".join(line) + " </s> <\l> ").encode('utf-8'))
    else:
        www.write('<l> ')
        print line
        line=line.decode('utf-8')
        for sentence in line.split():
            # www.write(word)
            str = u" ".join(jieba.cut(sentence))
            # print str
            www.write(('<s> ' + str + " </s> ").encode('utf-8'))
        www.write('</l> ')
www.write('</p>\n')

'''
import linecache

for yee in range(22125) :
    if yee == 0 :
        continue
    be=linecache.getline('/Users/Nini/Desktop/schoolproject/LyricsFile22124/LyricsFile/0list.txt',yee)
    af=linecache.getline('/Users/Nini/Desktop/schoolproject/1011_1000/format/0_1011_1000_flist.txt',yee)
    #print be
    #print af
    bef = be[0:len(be) - 1]
    aft = af[0:len(af) - 1]
    #print aft
    print bef
    f = open(bef, 'r')
    www = open(aft, 'w')

    data = f.readlines()
    for line in data:
        line = line.replace("　", " ")

        if line[0] == '\n':
            www.write('#')
        else:
            www.write('<')
            print line
            line.decode('utf-8')
            for word in line:
                if word.isspace():
                    www.write('/')
                elif word != '\n':
                    www.write(word)
            www.write('>')
'''

#re.search('[a-zA-z]',line)