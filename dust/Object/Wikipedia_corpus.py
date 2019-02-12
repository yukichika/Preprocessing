#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import Delete

INPUT_DIR = XXXXXXXXXX
filelist = os.listdir(INPUT_DIR)
OUTPUT_DIR = XXXXXXXXXX

totalcount = 0#総数
for list in filelist:
    print("ファイル名：" + list)
    with open(os.path.join(INPUT_DIR,list),'r',encoding='UTF-8') as file_in:#読み込み用
        lines = file_in.readlines()
        for i,line in enumerate(tqdm(lines)):
            if line[0:4] == "<doc":
                begin = i#初めの行数
                totalcount += 1

                title = line.split("=")[-1]
                title = re.sub(">","",title)
                title = re.sub("\"","",title)
                title = Delete.title(title)

                title = title + "(" + str(totalcount) + ")"

            if line[0:4] == "</do":
                end = i#終わりの行数

                text = ""
                for j in range(begin+2,end):
                    if lines[j][0] == "\n":
                        lines[j][0] == ""
                    else:
                        text += lines[j]

                with open(os.path.join(OUTPUT_DIR,title + ".txt"),'w',encoding='UTF-8') as file_out:
                    file_out.write(text)
