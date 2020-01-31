#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/31 13:15
# @Author : diyhome
# @Site : https://gitee.com/jingjiangxueyuan_hmqs/
# @File : main.py
# @Software: PyCharm
from hal_data_clean import main
from get_counter import get_text

url = "https://www.zhihu.com/question/339011506"

if __name__ == '__main__':
    raw_data = get_text.get_json(url)
    for index in range(len(raw_data)):
        tmp = main(raw_data[index][1])
        print(tmp)
