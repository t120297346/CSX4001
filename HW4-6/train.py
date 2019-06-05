# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:43:41 2019

@author: user
"""

from gensim.models import word2vec
import jieba
import logging
from argparse import ArgumentParser
from sklearn.decomposition import PCA
from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence('segphase/segphases_{0}.txt'.format(2))
    model = word2vec.Word2Vec(sentences, size=100, alpha=0.0005,min_alpha=0.00001, min_count=20, iter=10)
    model.save("word2vec/word2vec_{0}.model".format(2))
def test():
    model = word2vec.Word2Vec.load('word2vec/word2vec_{0}.model'.format(2))
    phase = input("Please input a phase: ")
    out = model.similar_by_vector(str(phase),topn=10)
    word = []
    # for i in range(args.topn):
    #     word.append(" ".join(out[i][0]))
    try :
        os.path.isfile('tags.txt')
    except :
        open('tags.txt','wb')
    f = open('tags.txt', 'wb')
    for i in range(10):
        f.write(out[i][0]+" ")
        print(out[i][0])
    f.close()
    # phase2 = input("Please input another phase")
    # print(model.similarity(phase, phase2))
    # X = model[model.wv.vocab]
    # pca = PCA(n_components=2)
    # result = pca.fit_transform(X)

    # pyplot.scatter(result[:, 0], result[:, 1])
    # words = list(model.wv.vocab)
    # for i, word in enumerate(words):
    #     pyplot.annotate(word.encode('utf-8'), xy=(result[i, 0], result[i, 1]))
    # pyplot.show()

    # 讀取每首歌的前10個tags

    text = open('tags.txt').read()
    print(text)
    # 設定停用字(排除常用詞、無法代表特殊意義的字詞)
    # stopwords = {}.fromkeys(["書"])
    # 產生文字雲
    wc = WordCloud(font_path="NotoSerifCJKtc-Black.otf", #設置字體
               background_color="white", #背景顏色
               max_words = 2000 ,)      #停用字詞
    wc.generate(text)
    # 視覺化呈現
    plt.imshow(wc)
    plt.axis("off")
    # plt.figure(figsize=(10,6), dpi = 100)
    plt.show()
if __name__ == '__main__':
    #parser = ArgumentParser()
    #parser.add_argument("-n", "--novel", default=1,type=int)
    #parser.add_argument("-m", "--mode", default='train', type=str)
    #parser.add_argument("-t", "--topn", default=10, type=int)
    #args = parser.parse_args()
    main()
    test()