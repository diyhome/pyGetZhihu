#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/31 13:15
# @Author : diyhome
# @Site : https://gitee.com/jingjiangxueyuan_hmqs/
# @File : main.py
# @Software: PyCharm
url = "https://www.zhihu.com/question/339011506"

from get_counter import get_text

# 句子选择器
def filter_sentence(text):
    # 替换规则
    rules = ['<p class="ztext-empty-paragraph"><br/>', '<p>', '<blockquote>', '</blockquote>', '<h2>']
    tmp = text
    for key in rules:
        tmp = tmp.replace(key, '')
    tmp = tmp.replace('<br/', ' ')
    list = []

    # 断句并且挑选
    for row in tmp.split('</p>'):
        if "img" in row or "href" in row:
            continue
        remove_space = row.replace(' ', '')

        list.append(row)
        print(row)
    return list

if __name__ == '__main__':
    raw_data = get_text.get_json(url)
    for index in range(len(raw_data)):
        # 数据格式有理化
        tmp = filter_sentence(raw_data[index][1])