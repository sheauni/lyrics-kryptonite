# -*- coding: utf-8 -*-
import re


punc = "ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏˇˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ\￣︶▽ρ┬σ㊣．€↑↓↘↖↗↙→┴└┌♡《□■╬﹕。┘╭╮─▃▄▅▆▇█▉▊\╩╔╥◢◣●○ο◆◇﹉☆★〉〈﹒°∴◎⊙※║══１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＱＷＥＲＴＹＵＩＯＰＬＫＪＨＧＦＤＳＡＺＸＣＶＢＮＭ0123456789！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
punc = punc.decode("utf-8")
a=0
b=0
c=0
d=0
e=0
f=0
g=0

for i in range(1,59263):
    print i
    file = open('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/lyrics/'+str(i)+'.txt','r')
    new = open('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/GarbageRemoved/'+str(i)+'.txt','w')
    for s in file.readlines():
        if (not s.find('更多更詳盡歌詞')):
            print 'a'
            a+=1
            print s
            continue
        if (not s.find('作詞：')):
            print 'b'
            b+=1
            print s
            continue
        if (not s.find('作曲：')):
            print 'c'
            c+=1
            print s
            continue
        if (not s.find('編曲：')):
            print 'd'
            d+=1
            print s
            continue
        if (not s.find('提供歌詞')):
            print 'e'
            e+=1
            print s
            continue
        if (not s.find('提供動態歌詞')):
            print 'f'
            f+=1
            print s
            continue
        if (not s.find('http')):  
            print 'g'
            g+=1
            print s
            continue
        else:
            s = re.sub(ur"[%s]+" % punc, "", s.decode("utf-8"))
            print '----------'
            new.write(s.encode('utf-8'))
    print a
    print b
    print c
    print d
    print f
    print g
    file.close()
    new.close()
