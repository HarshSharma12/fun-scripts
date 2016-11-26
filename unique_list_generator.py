# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:00:28 2016

@author: HarshSharma12
@email: mail.hs.harsh@gmail.com
"""
from nltk.stem.snowball import SnowballStemmer
import os


def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist


fname = ''
exten = ''
fid = open(fname + exten, 'r')
a = fid.readlines()
print len(a)
fid.close()

listOrig = map(lambda x: x.lower(), a)
stemmer = SnowballStemmer("english")
stemmed = [stemmer.stem(word) for word in listOrig]
i = 0
for yy in listOrig:
    if yy in stemmed:
        i = i + 1

print i
fid = open(fname + '.txt', 'w')

b = unique_list(stemmed)
try:
    b.pop(b.index('\n'))
    b.pop(b.index('\t'))
except:
    print 'Finishing'
fid.writelines(b)
print len(b)
fid.close()

os.system("pause")
