#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
計数用プログラム
"""

from collections import Counter
import os
import math
import codecs
import sys
sys.path.append("..")
from Preprocessing import Wakati
from Preprocessing import File_operation

"""ファイル内の総単語数"""
def words_count(file):
    with codecs.open(file,'r','UTF-8','ignore') as file_in:
        sentence = file_in.read()
        words = Wakati.words_list(sentence)#全単語
        # words = Wakati.words_list_select(sentence)#品詞選択
        word_count = len(words)
    return word_count

"""ファイル内の語彙数"""
def vocabs_count(file):
    with codecs.open(file,'r','UTF-8','ignore') as file_in:
        sentence = file_in.read()
        words = Wakati.words_list(sentence)#全単語
        # words = Wakati.words_list_select(sentence)#品詞選択
        counter = Counter(words)
        vocab_count = len(counter)
    return vocab_count

"""ファイル内の文数"""
def sentences_count(file):
    with codecs.open(file,'r','UTF-8','ignore') as file_in:
        sentences = file_in.readlines()
        sentence_count = len(sentences)
    return sentence_count

"""ファイル内の総単語数、語彙数、文数"""
def all_count(file):
    with codecs.open(file,'r','UTF-8','ignore') as file_in:
        sentences = file_in.readlines()
    with codecs.open(file,'r','UTF-8','ignore') as file_in:
        sentence = file_in.read()
    words = Wakati.words_list(sentence)#全単語
    # words = Wakati.words_list_select(sentence)#品詞選択

    word_count = len(words)
    counter = Counter(words)
    vocab_count = len(counter)
    sentence_count = len(sentences)
    return word_count,vocab_count,sentence_count

"""ディレクトリ内の全てのファイルの総単語数"""
def words_total(dir):
    filelists = File_operation.get_all_paths(dir)
    print("ファイル数：" + str(len(filelists)))
    totalwords = 0
    for file in filelists:
        totalwords += words_count(file)
    return totalwords

"""ディレクトリ内の全てのファイルの語彙数"""
def words_vocab(dir):
    filelists = File_operation.get_all_paths(dir)
    print("ファイル数：" + str(len(filelists)))
    totalwords = []
    for file in filelists:
        with codecs.open(file,'r','UTF-8','ignore')as file_in:
            sentence = file_in.read()
        totalwords.extend(Wakati.words_list(sentence))

    counter = Counter(totalwords)
    vocab_count = len(counter)
    return vocab_count

"""ディレクトリ内の全てのファイルの平均単語数"""
def words_average(dir):
    filelists = File_operation.get_all_paths(dir)
    print("ファイル数：" + str(len(filelists)))
    if len(filelists) == 0:
        averagewords = 0
    else:
        totalwords = 0
        for file in filelists:
            totalwords += words_count(file)
        averagewords = totalwords / len(filelists)
    return averagewords

"""ディレクトリ内の最大単語数とそのファイルの絶対パス"""
def words_max(dir):
    filelists = File_operation.get_all_paths(dir)
    print("ファイル数：" + str(len(filelists)))
    maxwords = 0
    name = ""
    for file in filelists:
        words = words_count(file)
        if words >= maxwords:
            maxwords = words
            name = file
    return maxwords,name

"""ディレクトリ内の最小単語数とそのファイルの絶対パス"""
def words_min(dir):
    filelists = File_operation.get_all_paths(dir)
    print("ファイル数：" + str(len(filelists)))
    if len(filelists) == 0:
        minwords = 0
        name = None
    else:
        minwords = math.inf
        for file in filelists:
            words = words_count(file)
            if words <= minwords:
                minwords = words
                name = file
    return minwords,name
