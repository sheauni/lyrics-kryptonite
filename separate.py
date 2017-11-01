# -*- coding: utf-8 -*-

import jieba
import linecache


jieba.set_dictionary('/Library/Python/2.6/site-packages/jieba/dict.txt.big.txt')

for yee in range(1001) :
    if yee == 0 :
        continue
    be=linecache.getline('/Users/Nini/Desktop/schoolproject/LyricsFile22124/LyricsFile/0list.txt',yee)
    af=linecache.getline('/Users/Nini/Desktop/schoolproject/1011_1000/1011_1000_separated/0_1011_1000_list.txt',yee)
    #print be
    #print af
    bef = be[0:len(be) - 1]
    aft = af[0:len(af) - 1]
    #print aft
    print bef
    content = open(bef, 'rb').read()
    f = open(aft, 'w')
    words = jieba.cut(content, cut_all=False)
    for word in words:
        #print word
        www = word.encode('utf-8')
        f.write(www)
        f.write(' ')
    f.write('\n')

"""
    c = []
    with open(bef) as f:
        for line in f.readlines():
            c.append(line.split())

    dictionary = list()
    for pair in c:
        seg = list(jieba.cut(pair[0]))
        dictionary.append([int(pair[0]) - 1, seg])

    # 生成分词后的PICC文本
    with open("aft", "w") as f:
        for pair in dictionary:
            f.write(" ".join(pair[1]).encode('utf8'))
            f.write("\n")

"""