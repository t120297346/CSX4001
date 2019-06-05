# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:40:34 2019

@author: user
"""

import jieba 
import codecs
import os
from argparse import ArgumentParser

def main():
    f = codecs.open('novel/novel_{0}.txt'.format(2), 'r', 'utf-8')
    textseg=[]
    text = ''
    jieba.load_userdict("dict/user_dict_{0}".format(1))
    seg = jieba.cut(f.readlines()[0],cut_all=False)
    for s in seg:
        textseg.append(s)
    fileseg ='segphase/segphases_{0}.txt'.format(2)
    try:
        os.path.isfile(fileseg)
    except:
        open(fileseg,'wb')
    with open(fileseg,'wb') as fW:
        for i in range(len(textseg)):
            fW.write(textseg[i].encode('utf-8'))
            fW.write('\n'.encode('utf-8'))


main()
