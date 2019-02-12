#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import File_operation

INPUT_DIR = XXXXXXXXXX
filelist = os.listdir(INPUT_DIR)
OUTPUT_DIR = rXXXXXXXXXX

with open(os.path.join(OUTPUT_DIR,"Livedoor_info.csv"),'w',encoding='UTF-8-sig') as file_out:#書き込み用
    for list in tqdm(filelist):
        count = 0
        print("ジャンル：" + list)
        filelists = File_operation.get_all_paths(os.path.join(INPUT_DIR,list))
        file_out.write("URL,投稿日時,ジャンル,タイトル\n")
        for file in filelists:
            count += 1
            with open(file,'r',encoding='UTF-8') as file_in:#読み込み用
                lines = file_in.readlines()
                file_out.write(lines[0].replace("\n","").replace(",","") + "," + lines[1].replace("\n","").replace(",","") + "," + list + "," + lines[2].replace("\n","").replace(",","") + "\n")
