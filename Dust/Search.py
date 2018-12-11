#!/usr/bin/env python3
# -*- coding: utf-8 -*

import os
import time
import sys
sys.path.append("..")
from Preprocessing import File_operation

"""タイトル検索（単数）"""
# query = "ワガドゥーグー"
# SERCH_DIR = XXXXXXXXXX
# OUTPUT_DIR = XXXXXXXXXX
#
# filelist = File_operation.get_all_paths(SERCH_DIR)
#
# targetcount = 0
# with open(os.path.join(OUTPUT_DIR,query + ".txt"),'w',encoding='UTF-8')as file_out:
# 	for list in filelist:
# 		if not list.find(query) == -1:
# 			file_out.write(list + "\n")
# 			targetcount +=1
#
# 	if targetcount == 0:
# 		file_out.write("Target is nothing.")
#
# print("query:" + query)
# print("ヒット数 {} / {}".format(targetcount,len(filelist)))

"""タイトル検索（複数）"""
# keyword = "指定した作者の作品"
# OUTPUT_DIR = XXXXXXXXXX
# INPUT_FILE = os.path.join(OUTPUT_DIR,"query.txt")
# SERCH_DIR = XXXXXXXXXX
#
# with open(INPUT_FILE,'r',encoding='UTF-8-sig')as file_in:
# 	lines = file_in.readlines()
# filelist = File_operation.get_all_paths(SERCH_DIR)
#
# with open(os.path.join(OUTPUT_DIR,keyword + ".txt"),'w',encoding='UTF-8')as file_out:
# 	print("クエリ数：" + str(len(lines)))
# 	for line in lines:
# 		start = time.time()
#
# 		targetcount = 0
# 		if line == "\n":
# 			continue
# 		else:
# 			query = line[0:-1]
#
# 		file_out.write("<" + query + ">\n")
#
# 		for list in filelist:
# 			if not list.find(query) == -1:
# 				file_out.write(list + "\n")
# 				targetcount +=1
#
# 		if targetcount == 0:
# 			file_out.write(query + " is nothing." + "\n")
#
# 		file_out.write("\n")
#
# 		print("query:" + query)
# 		print("ヒット数 {} / {}".format(targetcount,len(filelist)))
#
# 		elapsed_time = time.time() - start
# 		print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

"""全文検索（単数）"""
# query = "日本酒"
# SERCH_DIR = XXXXXXXXXX
# OUTPUT_DIR = XXXXXXXXXX
#
# filelist = File_operation.get_all_paths(SERCH_DIR)
# targetcount = 0
# with open(os.path.join(OUTPUT_DIR,query + "_text.txt"),'w',encoding='UTF-8') as file_out:
# 	start = time.time()
# 	for list in filelist:
# 		with open(list,'r',encoding='UTF-8') as file_in:
# 			sentenses = file_in.read()
# 			if not sentenses.find(query) == -1:
# 				file_out.write(list + "\n")
# 				targetcount +=1
# 	if targetcount == 0:
# 		file_out.write("Target is nothing.")
# 	elapsed_time = time.time() - start
# 	print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
#
# print("query:" + query)
# print("ヒット数 {} / {}".format(targetcount,len(filelist)))

"""全文検索（複数）"""
# keyword = "酒とつまみ"
# OUTPUT_DIR = XXXXXXXXXX
# INPUT_FILE = os.path.join(OUTPUT_DIR,"query.txt")
# SERCH_DIR = XXXXXXXXXX
#
# with open(INPUT_FILE,'r',encoding='UTF-8-sig')as file_in:
# 	lines = file_in.readlines()
# filelist = File_operation.get_all_paths(SERCH_DIR)
#
# with open(os.path.join(OUTPUT_DIR,keyword + "_text.txt"),'w',encoding='UTF-8')as file_out:
# 	print("クエリ数：" + str(len(lines)))
# 	for line in lines:
# 		start = time.time()
#
# 		targetcount = 0
# 		if line == "\n":
# 			continue
# 		else:
# 			query = line[0:-1]
#
# 		file_out.write("<" + query + ">\n")
# 		print("query:" + query)
#
# 		for list in filelist:
# 			with open(list,'r',encoding='UTF-8') as file_in:
# 				sentenses = file_in.read()
# 				if not sentenses.find(query) == -1:
# 					file_out.write(list + "\n")
# 					targetcount +=1
#
# 		if targetcount == 0:
# 			file_out.write(query + " is nothing." + "\n")
#
# 		file_out.write("\n")
#
# 		print("query:" + query)
# 		print("ヒット数 {} / {}".format(targetcount,len(filelist)))
#
# 		elapsed_time = time.time() - start
# 		print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
