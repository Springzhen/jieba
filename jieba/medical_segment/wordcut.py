# -*- coding: UTF-8 -*-

from load_dict import *
import jieba
import jieba.posseg as pseg


def word_cut(sentence):
    jieba.load_userdict('./dict/temp.txt')
    outdata = [[i.word,i.flag] for i in pseg.cut(sentence,HMM=False)]
    return outdata


if __name__=="__main__":
    s = u'''患者近来感觉头痛、脑热，体温30摄氏度'''
    print(word_cut(s))
