#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zenhan
import re
import MeCab

class Sentense():

    def sentence(text):

        def __init__(self):
            self.sentence_lists = []

        #文分割
        #@params:文字列
        #@return:文が要素のリスト
        def sentence(text):
            #エスケープシーケンス削除
            text = text.replace("\r","").replace("\n","")
            if not line == "\n":
                


class Delete():

    def __init__(self):
        #削除するunicode文字列=>ひらがな・カタカナ・アルファベット・漢字以外
        self.u_code = r'[\u0000-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u3004\u3007-\u303F\u3099-\u30A0\u30FB\u30FD-\u4DFF\uA000-\uE0FFF]'
        #全unicode文字列
        self.all_u_code = r'[\u0000-\uE0FFF]'

    #文字列の正規化
    #@params:文字列
    #@return:正規化された文字列
    def normalize(self,text):
        #アルファベット：全角=>半角
        text = zenhan.z2h(text,mode=1)
        #数字：全角=>半角
        text = zenhan.z2h(text,mode=2)
        #カタカナ：半角=>全角
        text = zenhan.h2z(text,mode=4)
        return text

    #記号削除
    #@params:文字列
    #@return:正規化、記号削除後の文字列
    def del_symbol(self,text):
        #文字列の正規化
        text = self.normalize(text)
        #全unicode文字列の削除
        symbol = re.sub(self.all_u_code,"",text)
        #指定したunicode文字列の削除
        text = re.sub(self.u_code,"",text)
        #unicode文字列以外を削除
        if(symbol != ""):
            text = re.sub("[%s]"%symbol,"",text)
        return text

class Wakati():

    def __init__(self):
        #MeCabのモード
        self.MECAB_MODE = "-Owakati"

    #分かち書き
    def wakati(text):
        tagger = MeCab.Tagger(self.MECAB_MODE)
        text = tagger.parse(text)
        return text

if __name__ == '__main__':
    delete = Delete()
    print(delete.normalize("１２３ｶﾀｶﾅ"))
    print(delete.del_symbol("あ＠あ：あ」あ」あ"))
