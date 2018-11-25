#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from tqdm import tqdm_notebook as tqdm
import sys
sys.path.append("..")
from Preprocessing import File_operation

INPUT = XXXXXXXXXX
OUTPUT_DIR = XXXXXXXXXX

totalcount = 0
dirlists = os.listdir(INPUT)
dirlists.sort()

with open(os.path.join(OUTPUT_DIR,"Aozorabunko_info.csv"),'w',encoding='UTF-8-sig') as file_in:
    file_in.write("番号" + "," +"作者" + "," + "作品名" + "\n")
    for dir in tqdm(dirlists):
        filelists = os.listdir(os.path.join(INPUT,dir))
        filelists.sort()
        for file in filelists:
            totalcount += 1
            name = file.split("\\")[-1].split(".")[0]
            file_in.write(str(totalcount) + "," + dir + "," + name + "\n")
