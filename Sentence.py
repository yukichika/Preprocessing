#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文に分割（新Wikipedia用）
・"。"で終わるのを1文と定義
・「」は1文としない（「」内に複数の文があると厳しい）→会話がない文書に用いていたから問題なし。
"""
def sentence(line):
    beginnumber = 0#文の最初の文字のインデックス
    sentence_lists = []#文を格納するリスト

    line = line.replace("\r","").replace("\n","")
    if not line == "\n":
        """文字列に"。"があるかの分岐"""
        if not line.find("。") == -1:
            for i,char in enumerate(line):
                if char == "。":
                    if not i == len(line)-1 :
                        """ "。"の次の文字が"」"であるかの分岐"""
                        if not line[i+1] == "」" :
                            sentence_lists.append(line[beginnumber:i+1])
                            beginnumber = i+1
                        else:
                            pass
                    else:
                        sentence_lists.append(line[beginnumber:i+1])
                        beginnumber = i+1
            sentence_lists.append(line[beginnumber:])
        else:
            sentence_lists.append(line)
        while sentence_lists.count("") > 0:
            sentence_lists.remove("")
    return sentence_lists

"""
文に分割（小説用）
・"。"で終わるのを1文と定義
・「」は1文としない（「」内に複数の文があっても大丈夫なように改良）
"""
def sentence_novel(line):
    beginnumber = 0#文の最初の文字のインデックス
    sentence_lists = []#文を格納するリスト

    line = line.replace("\r","").replace("\n","")
    if not line == "\n":
        """文字列に"。"があるかの分岐"""
        if not line.find("。") == -1:
            for i,char in enumerate(line):
                if char == "。":
                    if not i == len(line)-1 :
                        if  "「" in line[beginnumber:i] and  "」" in line[i+1:] :
                            if "」" in line[beginnumber:i]:
                                sentence_lists.append(line[beginnumber:i+1])
                                beginnumber = i+1
                            else:
                                continue
                        else:
                            sentence_lists.append(line[beginnumber:i+1])
                            beginnumber = i+1
                    else:
                        sentence_lists.append(line[beginnumber:i+1])
                        beginnumber = i+1
            sentence_lists.append(line[beginnumber:])
        else:
            sentence_lists.append(line)
        while sentence_lists.count("") > 0:
            sentence_lists.remove("")
    return sentence_lists

"""
文に分割（旧Wikipedia用）
・"。"、"！"、"？"で終わるのを1文と定義
・上記の記号が連続していても1文とする（Twitterなどでも使えそう）→正規化する手もある。
※多分使うことはない。
"""
def sentence_old(line):
    beginnumber = 0#文の最初の文字のインデックス
    sentence_lists = []#文を格納するリスト

    line = line.replace("\r","").replace("\n","")
    if not line == "\n" and not line == "":
        if not line.find("。") == -1 or not line.find("！") == -1 or not line.find("？") == -1:#文字列に「。」，「！」，「？」があるかの分岐
            for i,char in enumerate(line):
                if char == "。" or char == "！" or char == "？":
                    if not i == len(line)-1 :
                        if not line[i+1] == "。" and not line[i+1] == "！" and not line[i+1] == "？":#「。」，「！」，「？」の次がまた「。」，「！」，「？」ではないかの分岐
                            sentence_lists.append(line[beginnumber:i+1])
                            beginnumber = i+1
                        else:
                            pass
                    else:
                        sentence_lists.append(line[beginnumber:i+1])
                        beginnumber = i+1
            sentence_lists.append(line[beginnumber:])
        else:
            sentence_lists.append(line)
        while sentence_lists.count("") > 0:
            sentence_lists.remove("")
    return sentence_lists
