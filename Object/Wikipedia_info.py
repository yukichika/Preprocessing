#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import Delete
from Preprocessing import File_operation

INPUT_DIR = XXXXXXXXXX
filelist = os.listdir(INPUT_DIR)
OUTPUT_DIR = XXXXXXXXXX

totalcount = 0#総数
for list in filelist:
    print(list)
    with open(os.path.join(INPUT_DIR,list),'r',encoding='UTF-8') as file_in:#読み込み用
        with open(os.path.join(OUTPUT_DIR,list + ".csv"),'w',encoding='UTF-8-sig') as file_out:#書き込み用
            file_out.write("タイトル" + "," + "ID" + "," + "URL" + "\n")
            lines = file_in.readlines()
            for i,line in enumerate(lines):
                if line[0:4] == "<doc":
                    totalcount += 1
                    begin = i#初めの行数
                    #タイトル
                    title = line.split("=")[-1]
                    title = re.sub(">","",title)
                    title = re.sub("\"","",title)
                    title = Delete.title(title)
                    #ID
                    id = line.split("=")[1].split(" ")[0]
                    id = re.sub("\"","",id)
                    id = re.sub("<","",id)
                    #URL
                    url = line.split(" ")[2]
                    url = url[4:]
                    url = re.sub("\"","",url)

                    file_out.write(title + "," + id + "," + url + "\n")

print("総数：" + str(totalcount))
