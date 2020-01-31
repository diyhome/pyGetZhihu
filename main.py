#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/31 13:15
# @Author : diyhome
# @Site : https://gitee.com/jingjiangxueyuan_hmqs/
# @File : main.py
# @Software: PyCharm
url = "https://www.zhihu.com/question/339011506"

from get_counter import get_text
import string

# 断句并且挑选
sentence_add = ""

# 句子选择器
def filter_sentence(text):
    global sentence_add
    # 替换规则
    rules = ['<p class="ztext-empty-paragraph"><br/>', '<p>', '<blockquote>', '</blockquote>', '<h2>', '&#34;', '<br/>']
    rules_enter_chart = ['</h1>', '</h2>', '</h3>', '</h4>', '</p>']
    tmp = text
    for key in rules:
        tmp = tmp.replace(key, ' ')
    for key in rules_enter_chart:
        tmp = tmp.replace(key, '\n')
    list = []

    for row in tmp.split('\n'):

        # 筛选
        if row == '':
            continue
        if "img" in row or "href" in row:
            continue
        remove_space = row.replace(' ', '')
        start_num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

        # 句子开头拼接
        if remove_space.startswith(start_num):
            row = row.lstrip(string.digits).lstrip(".").lstrip("、").lstrip("//").lstrip()
            # 提取出处
            if '——' in row:
                row_tmp = row.split('——')
                list.append([row_tmp[0], row_tmp[-1]])
                continue
            elif '———' in row: #真有奇葩打三个的
                row_tmp = row.split('———')
                list.append([row_tmp[0], row_tmp[-1]])
                continue
            elif '－－' in row: #还有这种奇葩
                row_tmp = row.split('－－')
                list.append([row_tmp[0], row_tmp[-1]])
                continue
            list.append([row, "NULL"])
            # print("*"+row+"*")
            continue
        elif remove_space.startswith('—') or remove_space.startswith('－－'):
            row = remove_space.strip(string.digits).lstrip("——").lstrip("——")
            if sentence_add != '':
                list.append([sentence_add.lstrip("\n"), row])
                sentence_add = ""
            list[len(list) - 1][1] = row
            continue  # 句子出处,应该追加到上面那个地方
        else:
            sentence_add = sentence_add + "\n" + row

    return list


if __name__ == '__main__':
    raw_data = get_text.get_json(url)
    for index in range(len(raw_data)):
        # 数据格式有理化
        print("-----------------------------------------------")
        tmp = filter_sentence(raw_data[index][1])
        if sentence_add != '':
            tmp.append([sentence_add, "NULL"])
            sentence_add = ""
        print(tmp)
