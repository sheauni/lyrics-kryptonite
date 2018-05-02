# trips/views.py

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django import template
import gensim
import re
import jieba
import numpy
from sklearn.preprocessing import normalize

punc = "ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏˇˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ\￣︶▽ρ┬σ㊣．€↑↓↘↖↗↙→┴└┌♡《□■╬﹕。┘╭╮─▃▄▅▆▇█▉▊\╩╔╥◢◣●○οO◆◇﹉☆★〉〈﹒°∴◎⊙※║══１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＱＷＥＲＴＹＵＩＯＰＬＫＪＨＧＦＤＳＡＺＸＣＶＢＮＭ0123456789！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
jieba.set_dictionary("C:/Users/user/schoolwork/dict.txt.big.txt")  # JIEBA 簡體轉繁體的字典路徑
d2v_model = gensim.models.doc2vec.Doc2Vec.load("C:/Users/user/schoolwork/model/20171220.vec")

d2v = normalize(numpy.array(d2v_model.docvecs), norm='max', axis=1, copy=True, return_norm=False)
song_name = open("C:/Users/user/schoolwork/song_list.txt", 'r', encoding = 'utf-8' ).readlines()




def test(request):
    return render(request, 'test.html', {'current_time': str(datetime.now()), })



def test2(request):
    request.encoding = 'utf-8'
    reply = None
    if "text" in request.POST:  # ans['rlt']=request.POST["text"]      for line in request.POST["text"]
        reply = request.POST["text"]
    ans = {'input': reply}


    biggest = 0
    song = 0
    www = open("C:/Users/user/schoolwork/visitor.txt", 'w')    #使用者輸入字串存入的 txt 路徑
    www.write('<p> ')
    line = re.sub(r"[%s]+" % punc, "", reply)  #.decode("utf-8")

    line = line.strip(' ')
    if re.search('[a-zA-z]', line) is not None:
        line = jieba.cut(line)
        line = filter(lambda x: not x.isspace(), line)
        www.write(('<l> <s> ' + u" ".join(line) + " </s> <\l> "))      #.encode('utf-8')
    else:
        www.write('<l> ')
        for sentence in line.split():
            st = u" ".join(jieba.cut(sentence))
            www.write(('<s> ' + st + " </s> "))
        www.write('</l> ')
    www.close()

    f = open("C:/Users/user/schoolwork/visitor.txt", 'r')    #使用者輸入字串存入的 txt 路徑

    inputvec = d2v_model.infer_vector(f)

    for i in range(0, 59262):
        docvec = d2v[i]
        inner = inputvec.dot(docvec)
        if inner > biggest:
            biggest = inner
            song = i + 1
    mostsimilar = open( "C:/Users/user/schoolwork/lyrics/" + str(song+1) + '.txt','r' , encoding = 'utf-8' ).readlines()  #歌詞路徑
    mostsimilar = "".join(mostsimilar)
    result = song_name[song].split(',')
    ans = {'rlt': mostsimilar, 'name':result[1], 'author':result[2]}
    return render(request, "test.html", ans)
