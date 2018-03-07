# -*- coding: utf-8 -*-

import gensim
import re
import jieba
import numpy
#import array
from sklearn.preprocessing import normalize
import codecs
from time import clock
#import pygame


punc = "ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏˇˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ\￣︶▽ρ┬σ㊣．€↑↓↘↖↗↙→┴└┌♡《□■╬﹕。┘╭╮─▃▄▅▆▇█▉▊\╩╔╥◢◣●○οO◆◇﹉☆★〉〈﹒°∴◎⊙※║══１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＱＷＥＲＴＹＵＩＯＰＬＫＪＨＧＦＤＳＡＺＸＣＶＢＮＭ0123456789！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
punc = punc.decode("utf-8")

jieba.set_dictionary('/Library/Python/2.6/site-packages/jieba/dict.txt.big.txt')

#d2v_model = gensim.models.doc2vec.Doc2Vec.load('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/tryyyyy.vec')
d2v_model = gensim.models.doc2vec.Doc2Vec.load('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/model/20171220.vec')

#d2v=d2v_model.docvecs
d2v=normalize(numpy.array(d2v_model.docvecs),norm='max',axis=1,copy=True, return_norm=False)
song_name = open('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/song_list.txt','r').readlines()
#song_name = open('/Users/Nini/Desktop/schoolproject/LyricsFile22124/DatasetList_20140611.txt','r').readlines()

USER_INPUTS = "/Users/Nini/Desktop/schoolproject/1011_1000/lyrics-kryptonite/user_emotion.txt"
with codecs.open(USER_INPUTS, 'r', encoding='utf-8') as file:  # open(USER_INPUTS, 'r')
    start = clock()
    for line in file.readlines():

        biggest=0
        song=0


        www=open('/Users/Nini/Desktop/schoolproject/LyricsFile22124/say.txt','w')
        #line=raw_input('輸入一句話：')
        www.write('<p> ')
        line = re.sub(ur"[%s]+" % punc, "", line.encode('utf-8').decode("utf-8"))
        print line+','
        line = line.strip(' ')
        if re.search('[a-zA-z]', line) is not None:
            line = jieba.cut(line)
            line = filter(lambda x: not x.isspace(), line)
            www.write(('<l> <s> ' + u" ".join(line) + " </s> <\l> ").encode('utf-8'))
        else:
            www.write('<l> ')
                    # print line
                    # line = line.decode('utf-8')
            for sentence in line.split():
                        # www.write(word)
                st = u" ".join(jieba.cut(sentence))
                        # print str
                www.write(('<s> ' + st + " </s> ").encode('utf-8'))
            www.write('</l> ')
        www.close()

        f=open('/Users/Nini/Desktop/schoolproject/LyricsFile22124/say.txt','r')
        #print d2v_model.docvecs.most_similar(f)
        inputvec = d2v_model.infer_vector(f)

        for i in range(0,59262):
            docvec = d2v[i]

            '''
            inner = 0
            for j in range(0,300):
                k=inputvec[j]*docvec[j]
                inner+=k
            '''
            inner = inputvec.dot(docvec)
            if inner>biggest:
                biggest=inner
                song=i+1
        print str(biggest)+','
        #print str(song)+','
        print song_name[song]
        #mostsimilar=open('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/GarbageRemoved/'+str(song)+'.txt','r').readlines()
        #for line in mostsimilar:
        #    print line
        #print d2v_model.docvecs[song-1]
    finish = clock()
    print (finish - start)