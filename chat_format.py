# -*- coding: utf-8 -*-
import jieba     #分詞
import re        #用於清除標點

punc = "ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏˇˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ\￣︶▽ρ┬σ㊣．€↑↓↘↖↗↙→┴└┌♡《□■╬﹕。┘╭╮─▃▄▅▆▇█▉▊\╩╔╥◢◣●○ο◆◇﹉☆★〉〈﹒°∴◎⊙※║══１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＱＷＥＲＴＹＵＩＯＰＬＫＪＨＧＦＤＳＡＺＸＣＶＢＮＭ0123456789！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
punc = punc.decode("utf-8")

jieba.set_dictionary('/Library/Python/2.6/site-packages/jieba/dict.txt.big.txt')
#www = open('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/correct_format.txt', 'w')
www = open("/Users/Nini/Desktop/schoolproject/1011_1000/lyrics-kryptonite/user_emotion_formatted.txt", 'w')



def main():
    #for i in range(1,59263):
    #    run('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/GarbageRemoved/'+str(i)+'.txt')
    run("/Users/Nini/Desktop/schoolproject/1011_1000/lyrics-kryptonite/user_emotion.txt")

def run( input ):
    f = open(input, 'r')
    data = f.readlines()
    www.write('<p> ')
    #前一行為空白
    pre_empty=0
    for line in data:
        #去除標點
        line = re.sub(ur"[%s]+" % punc, "", line.decode("utf-8"))
        print line
        #將前後空白符去除
        line = line.strip(' ')
        if len(line)==0:
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
            for sentence in line.split():
                str = u" ".join(jieba.cut(sentence))
                www.write(('<s> ' + str + " </s> ").encode('utf-8'))
            www.write('</l> ')
    www.write('</p>\n')

if __name__ == '__main__':
    main()
