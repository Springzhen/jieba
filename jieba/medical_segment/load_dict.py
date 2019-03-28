# -*- coding:utf-8 -*-
import jieba
import os


def rm_cache_file(cachefile):
    # 删除cache file 文件
    if os.path.exists(cachefile):
        os.remove(cachefile)
        print('rm %s succeed! ' % cachefile)
    else:
        print('no such file:%s' % cachefile)


def load_data():
    path = './dict/'
    txtlist = [p for p in os.listdir(path) if p.endswith('.txt')]
    for txt in txtlist:
        jieba.load_userdict(path + txt)
    

# rm_cache_file('jieba.cache')     
load_data()