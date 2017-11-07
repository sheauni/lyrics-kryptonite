# -*- coding: utf-8 -*-

import gensim

#loading the model
model = gensim.models.doc2vec.Doc2Vec.load('/Users/Nini/Desktop/schoolproject/LyricsFile22124/one_thousand.vec')
#start testing
#printing the vector of document at index 1 in docLabels
f=open('/Users/Nini/Desktop/schoolproject/LyricsFile22124/s2.txt','r').readlines()
i=0
for line in f:
    i+=1
    if i==1011:
        break
    elif i>1000:
        www = open('/Users/Nini/Desktop/schoolproject/LyricsFile22124/10songs/' + str(i) + '.txt', 'w')
        www.write(line)
        www.close()
        newvec = model.infer_vector(['/Users/Nini/Desktop/schoolproject/LyricsFile22124/10songs/' + str(i) + '.txt'])
        print newvec
        print '\n\n'

