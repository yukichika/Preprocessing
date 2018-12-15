#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shutil
import random
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import File_operation
from Preprocessing import Count

"""ランダムにファイルコピー"""
# filenumber = 340
# INPUT_DIR = XXXXXXXXXX
# OUTPUT_DIR = XXXXXXXXXX
# os.makedirs(OUTPUT_DIR,exist_ok=True)
#
# total = 0#総数
#
# filelist = File_operation.choice_file(INPUT_DIR,filenumber)
# for i,list in enumerate(filelist):
#     file = list.split("\\")[-1]
#     print(str(i+1) + ":" + file)
#     total += 1
#
#     shutil.copy2(list,os.path.join(OUTPUT_DIR,file))
#
# print("総数：" + str(total))

"""全てのファイルコピー"""
# INPUT_DIR = XXXXXXXXXX
# OUTPUT_DIR = XXXXXXXXXX
#
# filelist = File_operation.get_all_paths(INPUT_DIR)
# for i,list in (enumerate(tqdm(filelist))):
#     file = list.split("\\")[-1]
#
#     shutil.copy2(list,os.path.join(OUTPUT_DIR,file))
