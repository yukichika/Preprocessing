#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
文字列削除用プログラム
"""

import re
import os
import zenhan

"""
・全角半角を変換
・ひらがな，カタカナ，アルファベット，漢字以外を削除（Unicode一覧表に基づいて全て指定）
・Unicode非対応の文字を削除
"""
def delete_symbol(line):
	text = zenhan.z2h(line,mode=1)#アルファベット（全角→半角）
	text = zenhan.z2h(text,mode=2)#数字（全角→半角）
	text = zenhan.h2z(text,mode=4)#カタカナ（半角→全角）

	symbol = re.sub(r'[\u0000-\uE0FFF]',"",text)#unicode非対応の文字
	text = re.sub(r'[\u0000-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u3004\u3007-\u303F\u3099-\u30A0\u30FB\u30FD-\u4DFF\uA000-\uE0FFF]',"",text)#その他文字列削除
	"""unicode非対応の文字の削除"""
	if not symbol == "":
		text = re.sub("[%s]"%symbol,"",text)
	return text

"""
Wikipedia用
・全角半角を変換
・（文章）を削除
・ひらがな，カタカナ，アルファベット，漢字以外を削除（Unicode一覧表に基づいて全て指定）
"""
def delete_wikipedia(line):
	text = zenhan.z2h(line,mode=1)#アルファベット（全角→半角）
	text = zenhan.z2h(text,mode=2)#数字（全角→半角）
	text = zenhan.h2z(text,mode=4)#カタカナ（半角→全角）

	text = re.sub(r'\(.*?\)',"",text)#半角()を中身ごと削除
	text = re.sub(r'[\u0000-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u3004\u3007-\u303F\u3099-\u30A0\u30FB\u30FD-\u4DFF\uA000-\uE0FFF]',"",text)#その他文字列削除
	return text

"""
Twitter用
・全角半角を変換
・URL，ユーザー名，ハッシュタグを削除
・ひらがな，カタカナ，アルファベット，漢字以外を削除（Unicode一覧表に基づいて全て指定）
・Unicode非対応の文字を削除
"""
def delete_twitter(line):
	text = zenhan.z2h(line,mode=1)#アルファベット（全角→半角）
	text = zenhan.z2h(text,mode=2)#数字（全角→半角）
	text = zenhan.h2z(text,mode=4)#カタカナ（半角→全角）

	symbol = re.sub(r'[\u0000-\uE0FFF]',"",text)#unicode非対応の文字
	text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+',"",text)#URL
	text = re.sub(r'@[\w/:%#\$&\?\(\)~\.=\+\-…]+',"",text)#ユーザ名
	text = re.sub(r'#[\w/:%#\$&\?\(\)~\.=\+\-…]+',"",text)#ハッシュタグ
	text = re.sub(r'[\u0000-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u3004\u3007-\u303F\u3099-\u30A0\u30FB\u30FD-\u4DFF\uA000-\uE0FFF]',"",text)#その他文字列削除
	"""unicode非対応の文字の削除"""
	if not symbol == "":
		text = re.sub("[%s]"%symbol,"",text)
	return text

"""
青空文庫（小説）用
・全角半角を変換
・[文章]を削除
・《読み方》を削除
・ひらがな，カタカナ，アルファベット，漢字以外を削除（Unicode一覧表に基づいて全て指定）
"""
def delete_aozora(line):
	text = zenhan.z2h(line,mode=1)#アルファベット（全角→半角）
	text = zenhan.z2h(text,mode=2)#数字（全角→半角）
	text = zenhan.h2z(text,mode=4)#カタカナ（半角→全角）

	text = re.sub(r'\[.*?\]',"",text)#半角[]を中身ごと削除
	text = re.sub(r'\《.*?\》',"",text)#半角《》を中身ごと削除
	text = re.sub(r'[\u0000-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u3004\u3007-\u303F\u3099-\u30A0\u30FB\u30FD-\u4DFF\uA000-\uE0FFF]',"",text)#その他文字列削除
	return text

"""
ファイルのタイトル用
・エスケープシーケンスを削除
・HTML特殊文字を削除
・タイトルの長さ調節
・Windowsで使えない文字の対処
"""
def title(title):
	title = re.sub("\r","",title)
	title = re.sub("\n","",title)
	title = re.sub("\t","",title)
	#HTML-特殊文字の削除
	title = re.sub("&quot;","",title)
	title = re.sub("&amp;","",title)
	title = re.sub("&lt;","",title)
	title = re.sub("&gt;","",title)
	title = re.sub("&nbsp;","",title)
	title = re.sub("&copy;","",title)

	title = re.sub(r'[\\|/|:|?|.|*|"|<|>|\|]', '_', title)#タイトルに使えない文字の対処
	if len(title) >= 100:#タイトルが長すぎた時の対処
		title = title[0:100] + "~ext"

	"""Windows上で使えないファイル名の対処"""
	if title == "AUX" or title == "CON" or title == "NUL" or title == "PRN" or title == r"CLOCK$":
		title = "---" + title + "---"
	return title
