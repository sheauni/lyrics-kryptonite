# encoding=utf8
# -*- coding: utf-8 -*-
import codecs
import numpy as np
import re
import jieba
from gensim.models.doc2vec import TaggedLineDocument, Doc2Vec
import argparse
from sklearn.preprocessing import normalize

result = open('/Users/Nini/Desktop/schoolproject/0123_result.txt','w')
LYRIC = "/Users/Nini/Desktop/schoolproject/1206_lyrics_file/correct_format.txt"
LYRIC_DIR = '/Users/Nini/Desktop/schoolproject/'\
            '1206_lyrics_file/GarbageRemoved/'
USER_INPUTS = "/Users/Nini/Desktop/schoolproject/1011_1000/lyrics-kryptonite/user_emotion.txt"
N_SONG = 59262

punc = {ord(c): ord(" ") for c in u"""ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏˇˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢ
        ㄣㄤㄥㄦ\￣︶▽ρ┬σ㊣．€↑↓↘↖↗↙→┴└┌♡《□■╬﹕。┘╭╮─▃▄▅▆▇█▉▊\╩╔╥◢◣●○οO◆◇﹉☆★〉
        〈﹒°∴◎⊙※║══１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔ
        ｕｖｗｘｙｚＱＷＥＲＴＹＵＩＯＰＬＫＪＨＧＦＤＳＡＺＸＣＶＢＮＭ01234567
        89！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､
        、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!!#$%&\'()*
        +,-./:;<=>?@[\\]^_`{|}~""`]"""}


def parse_args():
    parser = argparse.ArgumentParser(description='Lyric hyper-parameter tuner')
    parser.add_argument('-s', '--size', type=int, default=300,
                        help='dimensionality of the feature vectors')
    parser.add_argument('-w', '--window', type=int, default=10,
                        help='maximum distance between the current and '
                        'predicted word within a sentence')
    parser.add_argument('--min-count', type=int, default=1,
                        help='ignore all words with total frequency '
                        'lower than this')
    parser.add_argument('--workers', type=int, default=4,
                        help='threads to train model (fast)')
    parser.add_argument('-dm', type=int, default=1,
                        help='1: distributed memory’ (PV-DM) is used.'
                        '0: distributed bag of words (PV-DBOW) is employed.')

    return parser.parse_args()

def train(args):
    documents = TaggedLineDocument(LYRIC)
    return Doc2Vec(documents, size=args.size, window=args.window,
                   min_count=args.min_count, workers=args.workers, dm=args.dm)


def predict(d2v_model, d2v, line):
    biggest = 0
    song = 0


    input = '<p> '
    print line
    #line.encode("utf-8")
    #line = unicode(line, 'utf8')
    #line = re.sub(ur"[%s]+" % punc, "", line)
    line = line.translate(punc)
    print line
    result.write(line.encode('utf-8'))

    line = line.strip(' ')
    if re.search('[a-zA-z]', line) is not None:
        line = jieba.cut(line)
        line = filter(lambda x: not x.isspace(), line)
        input += ('<l> <s> ' + u" ".join(line) + " </s> <\l> ").encode('utf-8')
    else:
        input += '<l> '
        # print line
        # line = line.decode('utf-8')
        for sentence in line.split():
            # www.write(word)
            st = u" ".join(jieba.cut(sentence))
            # print str
            input += ('<s> ' + st + " </s> ").encode('utf-8')
        input += ('</l> ')

    inputvec = d2v_model.infer_vector(input)
    print inputvec

    for i in range(0, N_SONG):
        docvec = d2v[i]
        inner = inputvec.dot(docvec)
        if inner > biggest:
            biggest = inner
            song = i + 1
    print str(biggest) + '\n'
    result.write(str(biggest).encode('utf-8'))
    print str(song) + '\n'
    result.write(str(song).encode('utf-8')+'\n'.encode('utf-8'))
    mostsimilar = open(LYRIC_DIR + str(song) + '.txt', 'r').readlines()
    for line in mostsimilar:
        print line
        result.write(line)
    v = d2v_model.docvecs[song - 1]
    #print v
    result.write(v)
    result.write('\n\n'.encode('utf-8'))


def predict_many(model):
    d2v = normalize(np.array(model.docvecs), norm='max', axis=1, copy=True, return_norm=False)
    with codecs.open(USER_INPUTS,'r',encoding='utf-8') as file:  #open(USER_INPUTS, 'r')
        for line in file.readlines():
            #line = unicode(line, 'utf8')
            predict(model,d2v , line)


if __name__ == '__main__':
    args = parse_args()
    model = train(args)
    predict_many(model)