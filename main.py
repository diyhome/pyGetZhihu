#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/31 13:15
# @Author : diyhome
# @Site : https://gitee.com/jingjiangxueyuan_hmqs/
# @File : main.py
# @Software: PyCharm
import jieba
from HALDataClean import DataClean
from rJson.g_json import GJson
from db_opreate.op_sql import Database
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        # 日期格式
fp = logging.FileHandler('pyzhihu.log', encoding='utf-8')
fs = logging.StreamHandler()
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用

url = "https://www.zhihu.com/question/339011506"
ListofInvaild = ['.', ',', '!', '。', '，', '！', '？', '“', '”', '"', '的', '你', '我', '他', '哪些', '她', '偏', '哪', '到', '觉得', '也', '有', '是', '或者']

def extract_keywords(title):
    title = title.replace(' ', '')
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
    db = Database()

    category_id_list = []

    # sentence_list = []
    # raw_data = pgs.get_json()
    # for index in range(len(raw_data)):
    #     tmp = dc.filter(raw_data[index][1])
    #     if tmp == []:
    #         continue
    #     sentence_list += tmp

    # 数据库分类处理
    keywords = extract_keywords("气贯长虹 唯美 诗词 这是")
    for key in keywords:
        db_ans = db.select_more("category", 'cname = "%s"' % key)
        if not db_ans:
            print("%s 不在数据库中" % key)
            cid = db.count("category")
            sql_op = dict()
            sql_op['cid'] = '%s' % str(cid + 1)
            sql_op['cname'] = '"%s"' % key
            sql_op['count'] = '0'
            category_id_list.append(cid + 1)
        else:
            category_id_list.append(int(db_ans[0]['cid']))