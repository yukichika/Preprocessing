#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
形態素解析に関するプログラム
"""

import MeCab
import os

"""分かち書き"""
def wakati(text):
	MECAB_MODE = "-Owakati"
	tagger = MeCab.Tagger(MECAB_MODE)
	result = tagger.parse(text)
	return result

"""品詞を選択して分かち書き(名詞，動詞，形容詞)"""
def wakati_select(text):
	tagger = MeCab.Tagger("-Ochasen")
	lines = tagger.parse(text).splitlines()
	result_list = []
	for line in lines:
		chunks = line.split('\t')
		if not chunks[0] == "\ufeff":#UTF-8の識別子\ufeffとEOS以外を選別
			if len(chunks) > 3 and (chunks[3].startswith('動詞') or chunks[3].startswith('形容詞') or (chunks[3].startswith('名詞'))):#品詞選択
				result_list.append(chunks[0])
			# elif chunks[0] == "BOS" or chunks[0] == "EOS":
			# 	result_list.append(chunks[0])
	result = (" ").join(result_list) + "\n"
	return result

"""文書内の総単語をリストで取得"""
def words_list(text):
    mecab = MeCab.Tagger("-Ochasen")
    lines = mecab.parse(text).splitlines()
    allwords = []
    for line in lines:
        chunks = line.split('\t')
        if not chunks[0] == "\ufeff":#UTF-8の識別子\ufeff
            allwords.append(chunks[0])
    return allwords

"""文書内の総単語（名詞、動詞、形容詞）をリストで取得"""
def words_list_select(text):#品詞選択
    mecab = MeCab.Tagger("-Ochasen")
    lines = mecab.parse(text).splitlines()
    keywords = []
    for line in lines:
        chunks = line.split('\t')
        if not chunks[0] == "\ufeff":#UTF-8の識別子\ufeffとEOS以外を選別
            if len(chunks) > 3:
                if chunks[3].startswith("名詞") or chunks[3].startswith("形容詞") or chunks[3].startswith("動詞"):
                    keywords.append(chunks[0])
            # elif chunks[0] == "BOS" or chunks[0] == "EOS":
            #     keywords.append(chunks[0])
    return keywords
