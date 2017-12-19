# -*- coding: utf-8 -*-
import re


punc = "ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏˇˋㄐㄑㄒㄓㄔㄕㄖˊㄗㄘㄙ˙ㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ\￣︶▽ρ┬σ㊣．€↑↓↘↖↗↙→┴└┌♡《□■╬﹕。┘╭╮─▃▄▅▆▇█▉▊\╩╔╥◢◣●○οO◆◇﹉☆★〉〈﹒°∴◎⊙※║══１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＱＷＥＲＴＹＵＩＯＰＬＫＪＨＧＦＤＳＡＺＸＣＶＢＮＭ0123456789！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
punc = punc.decode("utf-8")


for i in range(1,59263):
    print i
    file = open('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/lyrics/'+str(i)+'.txt','r')
    new = open('/Users/Nini/Desktop/schoolproject/1206_lyrics_file/GarbageRemoved/'+str(i)+'.txt','w')
    for s in file.readlines():
        if (not s.find('更多更詳盡歌詞')):  # or s.find('作詞：') or s.find('作曲：') or s.find('編曲：'))
            print 'a'
            print s
            continue
        if (not s.find('作詞：')):  # or s.find('作詞：') or s.find('作曲：') or s.find('編曲：'))
            print 'b'
            print s
            continue
        if (not s.find('作曲：')):  # or s.find('作詞：') or s.find('作曲：') or s.find('編曲：'))
            print 'c'
            print s
            continue
        if (not s.find('編曲：')):  # or s.find('作詞：') or s.find('作曲：') or s.find('編曲：'))
            print 'd'
            print s
            continue
        if (not s.find('提供歌詞：')):  # or s.find('作詞：') or s.find('作曲：') or s.find('編曲：'))
            print 'e'
            print s
            continue
        if (not s.find('提供動態歌詞：')):  # or s.find('作詞：') or s.find('作曲：') or s.find('編曲：'))
            print 'f'
            print s
            continue
        if (not s.find('http')):  # or s.find('作詞：') or s.find('作曲：') or s.find('編曲：'))
            print 'g'
            print s
            continue
        else:
            s = re.sub(ur"[%s]+" % punc, "", s.decode("utf-8"))
            print '----------'
            new.write(s.encode('utf-8'))
    file.close()
    new.close()