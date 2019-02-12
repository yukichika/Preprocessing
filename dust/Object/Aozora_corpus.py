#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import File_operation
from Preprocessing import Sentence
from Preprocessing import Delete

INPUT_DIR = XXXXXXXXXX
OUTPUT_DIR = XXXXXXXXXX
filelist = File_operation.get_all_paths(INPUT_DIR)

totalcount = 0
for k,list in enumerate(tqdm(filelist)):
    try:
        with open(list,'r',encoding='ANSI') as file_in:
            file = list.split("\\")[-1]
            lines = file_in.readlines()

            for i,line in enumerate(lines):
                if line[0:3] == "---":
                    lines[0:i+1] = ""
                    break

            for i,line in enumerate(lines):
                if line[0:3] == "---":
                    lines[0:i+1] = ""
                    break

            for i,line in enumerate(lines):
                if line[0:2] == "底本":
                    lines[i:] = ""
                    break

            text = ""
            with open(os.path.join(OUTPUT_DIR,file),'w',encoding='UTF-8') as file_out:
                for i,line in enumerate(lines):
                    if not line == "" and not line == "\n":
                        text += line

                file_out.write(text)

    except Exception as e:
        print(e)
        pass
