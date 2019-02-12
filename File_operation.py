#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ファイル操作用プログラム
"""

import os
import re
import glob
import random
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import Wakati

"""ディレクトリ内の全てのファイルの絶対パスを取得"""
def get_all_paths(directory):
    corpus = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            corpus.append(os.path.join(root, file))
    return corpus

"""ディレクトリ内のファイルをランダムに選択し，絶対パスを取得"""
def choice_file(dir_path,num):
    files = get_all_paths(dir_path)
    filelists = random.sample(files,num)
    return filelists

"""複数のテキストファイルを1つに統合"""
def concate(INPUT_DIR,OUTPUT_DIR,name):
    lists = get_all_paths(INPUT_DIR)
    with open(os.path.join(OUTPUT_DIR,name),'w',encoding='UTF-8') as file_out:
        print("総ファイル数:" + str(len(lists)))
        for file in tqdm(lists):
            with open(file,'r',encoding='UTF-8-sig') as file_in:
                lines = file_in.readlines()
                for line in lines:
                    file_out.write(line)
                    if line == lines[-1] and not line[-1] == "\n" and not file == lists[-1]:
                        file_out.write("\n")

"""複数のテキストファイルを分かち書きして1つに統合"""
def concate_wakati(INPUT_DIR,OUTPUT_DIR,name):
    lists = get_all_paths(INPUT_DIR)
    with open(os.path.join(OUTPUT_DIR,name),'w',encoding='UTF-8') as file_out:
        print("総ファイル数:" + str(len(lists)))
        for file in tqdm(lists):
            with open(file,'r',encoding='UTF-8-sig') as file_in:
                lines = file_in.readlines()
                for line in lines:
                    text = Wakati.wakati(line)
                    if line == lines[-1] and file == lists[-1]:
                        text = text.replace("\n","")
                        file_out.write(text)
                    else:
                        file_out.write(text)
