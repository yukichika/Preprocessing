#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from tqdm import tqdm
import sys
sys.path.append("..")
from Preprocessing import File_operation

pre_word = "_"#変更前の文字列
aft_word = "_pca2"#変更後の文字列
INPUT_DIR = XXXXXXXXXX

Files = File_operation.get_all_paths(INPUT_DIR)
for file in tqdm(Files):
    newname = file.replace(pre_word,aft_word)
    os.rename(file, newname)
