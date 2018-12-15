#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import File_operation

INPUT_DIR = XXXXXXXXXX
filelist = File_operation.get_all_paths(INPUT_DIR)
OUTPUT_DIR = XXXXXXXXXX

with open(os.path.join(OUTPUT_DIR,"all_path(EncyclopediaMypedia58312).csv"),'w',encoding='UTF-8-sig')as file_out:
    for i,file in enumerate(tqdm(filelist)):
        name = file.replace(",","")
        file_out.write(str(i+1) + "," + name + "\n")
