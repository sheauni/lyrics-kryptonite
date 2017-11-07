# -*- coding: utf-8 -*-
import jieba
import re


punc = "ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏˇˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ\￣︶▽ρ┬σ㊣．€↑↓↘↖↗↙→┴└┌♡《□■╬﹕。┘╭╮─▃▄▅▆▇█▉▊\╩╔╥◢◣●○οO◆◇﹉☆★〉〈﹒°∴◎⊙※║══１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＱＷＥＲＴＹＵＩＯＰＬＫＪＨＧＦＤＳＡＺＸＣＶＢＮＭ0123456789！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
punc = punc.decode("utf-8")

jieba.set_dictionary('/Library/Python/2.6/site-packages/jieba/dict.txt.big.txt')
www = open('/Users/Nini/Desktop/schoolproject/LyricsFile22124/s2.txt', 'w')


def main():
    with open("/Users/Nini/Desktop/schoolproject/LyricsFile22124/LyricsFile/0list.txt",'r') as lyrics:
        for filename in lyrics.readlines():
            run(filename[:-2])
            print filename[:-2]

def run( input ):
    f = open(input, 'r')
    data = f.readlines()
    www.write('<p> ')
    pre_empty=0
    for line in data:
        line = re.sub(ur"[%s]+" % punc, "", line.decode("utf-8"))
        print line
        line = line.strip(' ')
        if len(line) == 0:
            if pre_empty==0:
                pre_empty=1
                www.write('</p> <p> ')
        elif re.search('[a-zA-z]', line) is not None:
            pre_empty=0
            line = jieba.cut(line)
            line = filter(lambda x: not x.isspace(), line)
            www.write(('<l> <s> ' + u" ".join(line) + " </s> <\l> ").encode('utf-8'))
        else:
            pre_empty=0
            www.write('<l> ')
            # print line
            # line = line.decode('utf-8')
            for sentence in line.split():
                # www.write(word)
                str = u" ".join(jieba.cut(sentence))
                # print str
                www.write(('<s> ' + str + " </s> ").encode('utf-8'))
            www.write('</l> ')
    www.write('</p>\n')

if __name__ == '__main__':
    main()