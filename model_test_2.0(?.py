# -*- coding: utf-8 -*-


import numpy as np
import re
import jieba
from gensim.models.doc2vec import TaggedLineDocument, Doc2Vec
import argparse
from sklearn.preprocessing import normalize


LYRIC = "/Users/Nini/Desktop/schoolproject/1206_lyrics_file/correct_format.txt"
LYRIC_DIR = '/Users/Nini/Desktop/schoolproject/'\
            '1206_lyrics_file/GarbageRemoved/'
USER_INPUTS = "/Users/Nini/Desktop/schoolproject/1011_1000/lyrics-kryptonite/user_emotion.txt"
N_SONG = 59262

punc = """ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏˇˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢ
        ㄣㄤㄥㄦ\￣︶▽ρ┬σ㊣．€↑↓↘↖↗↙→┴└┌♡《□■╬﹕。┘╭╮─▃▄▅▆▇█▉▊\╩╔╥◢◣●○οO◆◇﹉☆★〉
        〈﹒°∴◎⊙※║══１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔ
        ｕｖｗｘｙｚＱＷＥＲＴＹＵＩＯＰＬＫＪＨＧＦＤＳＡＺＸＣＶＢＮＭ01234567
        89！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､
        、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!!#$%&\'()*
        +,-./:;<=>?@[\\]^_`{|}~""`]"""


def parse_args():
    parser = argparse.ArgumentParser(description='Lyric hyper-parameter tuner')
    parser.add_argument('-s', '--size', type=int, default=300,
                        help='dimensionality of the feature vectors')
    parser.add_argument('-w', '--window', type=int, default=5,
                        help='maximum distance between the current and '
                        'predicted word within a sentence')
    parser.add_argument('--min-count', type=int, default=5,
                        help='ignore all words with total frequency '
                        'lower than this')
    parser.add_argument('--workers', type=int, default=3,
                        help='threads to train model (fast)')
    parser.add_argument('-dm', type=int, default=1,
                        help='1: distributed memory’ (PV-DM) is used.'
                        '0: distributed bag of words (PV-DBOW) is employed.')

    return parser.parse_args()


def train(args):
    documents = TaggedLineDocument(LYRIC)
    return Doc2Vec(documents, size=args.size, window=args.window,
                   min_count=args.min_count, workers=args.workers, dm=args.dm)


def predict(d2v_model, line):
    biggest = 0
    song = 0

    d2v = normalize(np.array(d2v_model.docvecs),
                    norm='max', axis=1, copy=True, return_norm=False)

    input = '<p> '
    line = re.sub(ur"[%s]+" % punc, "", line.decode("utf-8"))
    print line

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

    for i in range(0, N_SONG):
        docvec = d2v[i]
        inner = inputvec.dot(docvec)
        if inner > biggest:
            biggest = inner
            song = i + 1
    print str(biggest) + '\n'
    print str(song) + '\n'
    mostsimilar = open(LYRIC_DIR + str(song) + '.txt', 'r').readlines()
    for line in mostsimilar:
        print line
    print d2v_model.docvecs[song - 1]


def predict_many(model):
    with open(USER_INPUTS, 'r') as file:
        for line in file.readlines():
            predict(model, line)


if __name__ == '__main__':
    args = parse_args()
    model = train(args)
    predict_many(model)