#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sys
sys.path.append("..")
from Preprocessing import File_operation
from Preprocessing import Delete
from Preprocessing import Sentence
from Preprocessing import Count

INPUT_DIR = XXXXXXXXXX
OUTPUT_DIR = XXXXXXXXXX

filelist = File_operation.get_all_paths(INPUT_DIR)

OUT1 = os.path.join(OUTPUT_DIR,"16~30")
os.makedirs(OUT1,exist_ok=True)
OUT2 = os.path.join(OUTPUT_DIR,"31~120")
os.makedirs(OUT2,exist_ok=True)
OUT3 = os.path.join(OUTPUT_DIR,"121~260")
os.makedirs(OUT3,exist_ok=True)
OUT4 = os.path.join(OUTPUT_DIR,"261~500")
os.makedirs(OUT4,exist_ok=True)
OUT5 = os.path.join(OUTPUT_DIR,"501~770")
os.makedirs(OUT5,exist_ok=True)
OUT6 = os.path.join(OUTPUT_DIR,"771~1100")
os.makedirs(OUT6,exist_ok=True)
OUT7 = os.path.join(OUTPUT_DIR,"1101~1700")
os.makedirs(OUT7,exist_ok=True)
OUT8 = os.path.join(OUTPUT_DIR,"1701~2200")
os.makedirs(OUT8,exist_ok=True)
OUT9 = os.path.join(OUTPUT_DIR,"2201~")
os.makedirs(OUT9,exist_ok=True)
OUT10 = os.path.join(OUTPUT_DIR,"0~8")
os.makedirs(OUT10,exist_ok=True)
OUT11 = os.path.join(OUTPUT_DIR,"9~15")
os.makedirs(OUT11,exist_ok=True)

totalcount = 0#総数
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0

for list in filelist:
    wordsnumber = Count.words_count(list)
    file = list.split("\\")[-1]
    totalcount += 1

    if wordsnumber <= 8:
        count10 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT10,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 9 and wordsnumber <= 15:
        count11 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT11,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 16 and wordsnumber <= 30:
        count1 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT1,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 31 and wordsnumber <= 120:
        count2 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT2,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 121 and wordsnumber <= 260:
        count3 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT3,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 261 and wordsnumber <= 500:
        count4 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT4,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 501 and wordsnumber <= 770:
        count5 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT5,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 771 and wordsnumber <= 1100:
        count6 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT6,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 1101 and wordsnumber <= 1700:
        count7 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT7,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 1701 and wordsnumber <= 2200:
        count8 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT8,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")
    elif wordsnumber >= 2201:
        count9 += 1
        with open(list,'r',encoding='UTF-8') as file_in:
            text = file_in.read()
            sentences = Sentence.sentence(text)
            with open(os.path.join(OUT9,file),'w',encoding='UTF-8')as file_out:
                for sentence in sentences:
                    file_out.write(Delete.delete_wikipedia(sentence) + "\n")

print("---抽出結果---")
print("0~8：" + str(count10))
print("9~15：" + str(count11))
print("16~30：" + str(count1))
print("31~120：" + str(count2))
print("121~260：" + str(count3))
print("261~500：" + str(count4))
print("501~770：" + str(count5))
print("771~1100：" + str(count6))
print("1101~1700：" + str(count7))
print("1701~2200：" + str(count8))
print("2201~：" + str(count9))
print("ファイル総数：" + str(totalcount))
