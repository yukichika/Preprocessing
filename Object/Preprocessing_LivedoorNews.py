#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import File_operation
from Preprocessing import Delete
from Preprocessing import Sentence

INPUT_DIR = XXXXXXXXXX
dirlist = os.listdir(INPUT_DIR)
OUTPUT_DIR = XXXXXXXXXX

for dir in dirlist:
    print(dir)
    filelist = File_operation.get_all_paths(os.path.join(INPUT_DIR,dir))
    for i,file in enumerate(tqdm(filelist)):
        with open(file,'r',encoding='UTF-8') as file_in:
            lines = file_in.readlines()
            title = lines[2]
            title = Delete.title(title)
            OUT = os.path.join(OUTPUT_DIR,dir)
            os.makedirs(OUT,exist_ok=True)
            with open(os.path.join(OUT,title + ".txt"),'w',encoding='UTF-8')as file_out:
                for line in lines[3:]:
                    if not line == "\n":
                        sentencelists = Sentence.sentence_novel(line)
                        for sentence in sentencelists:
                            text = Delete.delete_wikipedia(sentence)
                            if not text == "":
                                file_out.write(text + "\n")
