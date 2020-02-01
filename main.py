#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/31 13:15
# @Author : diyhome
# @Site : https://gitee.com/jingjiangxueyuan_hmqs/
# @File : main.py
# @Software: PyCharm
import jieba
from rJson.g_json import GJson
from HALDataClean import DataClean


url = "https://www.zhihu.com/question/339011506"
ListofInvaild = ['.', ',', '!', '。', '，', '！', '？', '“', '”', '"', '的', '你', '我', '他', '哪些', '她', '偏', '哪', '到', '觉得', '也', '有']

def extract_keywords(title):
    none_val = jieba.cut(title)
    tmp_str = "/".join(none_val)
    list_str = []
    for keyword in tmp_str.split("/"):
        if keyword in ListofInvaild:
            continue
        list_str.append(keyword)
    return list_str

if __name__ == '__main__':
    pgs = GJson(url)
    dc = DataClean()

    # sentence_list = []
    # raw_data = pgs.get_json()
    # for index in range(len(raw_data)):
    #     tmp = dc.filter(raw_data[index][1])
    #     if tmp == []:
    #         continue
    #     sentence_list += tmp
    print(extract_keywords("有哪些气贯长虹的诗词？"))