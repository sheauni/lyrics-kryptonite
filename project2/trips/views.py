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

"""def hello_world(request):
    return render(request, 'hello_world.html', {'current_time': str(datetime.now()), })
"""
def try2(request):
    return render(request, 'try2.html', {'current_time': str(datetime.now()), })

"""
def comment(request):
    return render(request, 'test_comment.html', {})

def home(request):
    post_list = Post.objects.all()
    return render( request, 'home.html', {'post_list': post_list,} )

def math(request, a, b):
    a = int(a)
    b = int(b)
    s=a+b
    d=a-b
    p=a*b
    q=a/b
    return render(request,'math.html', {'s': s, 'd': d, 'p': p, 'q': q})        # 叫出模板(template) -> 填寫模板(context+render) -> http回應(HttpResponse)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})"""

def go(request):
    request.encoding = 'utf-8'
    reply = None
    if "text" in request.POST :                                                                                                                        # ans['rlt']=request.POST["text"]      for line in request.POST["text"]
        reply = request.POST["text"]
    ans = {'input': reply}
    ans['rlt'], ans['num'] = emotion(reply)
    return render(request,"try2.html",ans)

def emotion(line):
    punc = "ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏˇˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ\￣︶▽ρ┬σ㊣．€↑↓↘↖↗↙→┴└┌♡《□■╬﹕。┘╭╮─▃▄▅▆▇█▉▊\╩╔╥◢◣●○οO◆◇﹉☆★〉〈﹒°∴◎⊙※║══１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＱＷＥＲＴＹＵＩＯＰＬＫＪＨＧＦＤＳＡＺＸＣＶＢＮＭ0123456789！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

    #punc = punc.decode("utf-8")

    jieba.set_dictionary("C:/Users/user/schoolwork/dict.txt.big.txt")

    d2v_model = gensim.models.doc2vec.Doc2Vec.load("C:/Users/user/schoolwork/model/model/20171220.vec")

    biggest = 0
    song = 0

    # d2v=d2v_model.docvecs
    d2v = normalize(numpy.array(d2v_model.docvecs), norm='max', axis=1, copy=True, return_norm=False)
    www = open("C:/Users/user/schoolwork/visitor.txt", 'w')
    www.write('<p> ')
    line = re.sub(r"[%s]+" % punc, "", line)  #.decode("utf-8")
    #print line
    line = line.strip(' ')
    if re.search('[a-zA-z]', line) is not None:
        line = jieba.cut(line)
        line = filter(lambda x: not x.isspace(), line)
        www.write(('<l> <s> ' + u" ".join(line) + " </s> <\l> "))      #.encode('utf-8')
    else:
        www.write('<l> ')
        # print line
        # line = line.decode('utf-8')
        for sentence in line.split():
            # www.write(word)
            st = u" ".join(jieba.cut(sentence))
            # print str
            www.write(('<s> ' + st + " </s> "))
        www.write('</l> ')
    www.close()

    f = open("C:/Users/user/schoolwork/visitor.txt", 'r')

    inputvec = d2v_model.infer_vector(f)

    for i in range(0, 59262):
        docvec = d2v[i]
        inner = 0
        for j in range(0, 300):
            k = inputvec[j] * docvec[j]
            inner += k
        if inner > biggest:
            biggest = inner
            song = i + 1
    #print str(biggest) + '\n'
    #print str(song) + '\n'
    mostsimilar = open( "C:/Users/user/schoolwork/lyrics/" + str(song) + '.txt','r' , encoding = 'utf-8' ).readlines()
    mostsimilar = "".join(mostsimilar)
    print( str(song) )
    return mostsimilar, str(song)

    #for line in mostsimilar:
    #    print line
    #print d2v_model.docvecs[song - 1]

