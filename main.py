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
ListofInvaild = ['.', ',', '!', '。', '，', '！', '？', '“', '”', '"', '的', '你', '我', '他', '哪些', '她', '偏', '哪', '到', '觉得', '也', '有', '是', '或者', '很']

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

    sentence_list = []
    raw_data = pgs.get_json()
    for index in range(len(raw_data)):
        tmp = dc.filter(raw_data[index][1])
        if tmp == []:
            continue
        listtmp = [raw_data[index][0], tmp, raw_data[index][2]]
        sentence_list.append(listtmp)

    # 数据库分类处理
    keywords = extract_keywords("读起来很唯美的句子")
    for key in keywords:
        db_ans = db.select_more("category", 'cname = "%s"' % key)
        if not db_ans:
            cid = db.count("category")
            cid = cid + 1
            sql_op = dict()
            sql_op['cid'] = '%s' % str(cid)
            sql_op['cname'] = '"%s"' % key
            sql_op['count'] = '0'
            db.insert("category", sql_op)
            category_id_list.append(cid + 1)
            logging.info("%s 被添加进入分类表 && id: %d" % (key, cid))
        else:
            category_id_list.append(int(db_ans[0]['cid']))

        for content in sentence_list:
            sql_op = dict()
            sql_op['author'] = '"%s"' % content[0]
            sql_op['hot'] = '%s' % content[2]
            for text in content[1]:
                id = db.count("sentence") + 1
                sql_op['sid'] = '%s' % str(id)
                sql_op['content'] = '"%s"' % text[0]
                sql_op['howfrom'] = '"%s"' % text[1]
                db.insert("sentence", sql_op)
                logging.info(sql_op)
                cate_op = dict()
                cate_op['sentence_id'] = '%s' % str(id)
                for key_index in category_id_list:
                    cid = db.count("press_sentence") + 1
                    cate_op['id'] = '%s' % str(cid)
                    cate_op['category_id'] = '%s' % str(key_index)
                    db.insert("press_sentence", cate_op)
