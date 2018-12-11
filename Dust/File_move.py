#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shutil
import random
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import Count
from Preprocessing import File_operation

"""単語数によりファイル移動"""
# INPUT_DIR = XXXXXXXXXX
# OUTPUT_DIR = XXXXXXXXXX
#
# total = 0#総数
# count1 = 0
# count2 = 0
#
# OUT1 = os.path.join(OUTPUT_DIR,"0~8")
# os.makedirs(OUT1,exist_ok=True)
# OUT2 = os.path.join(OUTPUT_DIR,"9~15")
# os.makedirs(OUT2,exist_ok=True)
#
# filelist = os.listdir(INPUT_DIR)
# for i,list in enumerate(filelist):
#     word_count = Count.words_count(os.path.join(INPUT_DIR,list))
#     print(str(i+1) + ":" + list + "(" + str(word_count) + ")")
#     total += 1
#
#     if word_count >= 0 and word_count <= 8:
#         count1 += 1
#         shutil.move(os.path.join(INPUT_DIR,list),os.path.join(OUT1,list))
#     elif word_count >= 9 and word_count <= 15:
#         count2 += 1
#         shutil.move(os.path.join(INPUT_DIR,list),os.path.join(OUT2,list))
#
# os.rmdir(INPUT_DIR)
# print(OUT1 + ":" + str(count1))
# print(OUT2 + ":" + str(count2))
# print("総数：" + str(total))

"""ランダムにファイル移動"""
# filenumber = 170
# INPUT_DIR = XXXXXXXXXX
# OUTPUT_DIR = XXXXXXXXXX
# os.makedirs(OUTPUT_DIR,exist_ok=True)
#
# total = 0#総数
#
# filelist = File_operation.choice_file(INPUT_DIR,filenumber)
# for i,list in enumerate(tqdm(filelist)):
#     file = list.split("\\")[-1]
#     print(str(i+1) + ":" + file)
#     total += 1
#
#     shutil.move(list,os.path.join(OUTPUT_DIR,file))
#
# print("総数：" + str(total))

"""指定したパスからランダムにファイル移動"""
# filenumber = 3
# keyword = XXXXXXXXXX
# INPUT_FILE = XXXXXXXXXX
# OUTPUT = rXXXXXXXXXX
# OUTPUT_DIR = os.path.join(OUTPUT,keyword)
# os.makedirs(OUTPUT_DIR,exist_ok=True)
#
# total = 0#総数
#
# with open(INPUT_FILE,'r',encoding='UTF-8-sig')as file_in:
# 	lines = file_in.readlines()
#
# filelists = random.sample(lines,filenumber)
#
# for i,list in enumerate(filelists):
#     file = list.split("\\")[-1].replace("\n","")
#     path = list.replace("\n","")
#     print(str(i+1) + ":" + file)
#     total += 1
#
#     if os.path.exists(path):
#         shutil.move(path,os.path.join(OUTPUT_DIR,file))
#     else:
#         print("Not " + path)
#
# print("総数：" + str(total))

"""パスを指定してファイル移動"""
# keyword = XXXXXXXXXX
# INPUT_FILE = XXXXXXXXXX
# OUTPUT = XXXXXXXXXX
# OUTPUT_DIR = os.path.join(OUTPUT,keyword)
# os.makedirs(OUTPUT_DIR,exist_ok=True)
#
# with open(INPUT_FILE,'r',encoding='UTF-8-sig')as file_in:
# 	lines = file_in.readlines()
#
# total = 0#総数
# for i,line in enumerate(lines):
#     total += 1
#     if line == "\n":
#         continue
#     else:
#         path = line[0:-1]
#
#     file = path.split("\\")[-1]
#     print(str(i+1) + ":" + file)
#
#     if os.path.exists(path):
#         shutil.move(path,os.path.join(OUTPUT_DIR,file))
#     else:
#         print("Not " + path)
#
# print("総数：" + str(total))
