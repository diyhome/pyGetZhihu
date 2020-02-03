#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/1 10:47
# @Author : diyhome
# @Site : https://gitee.com/jingjiangxueyuan_hmqs/
# @File : HALDataClean.py
# @Software: PyCharm

import string
from bs4 import BeautifulSoup
from RJson.g_json import GJson


class DataClean:
    def __init__(self):
        self.sentence = ""
     
    def __filter_sentence(self, text):
        # for key in self.r_rules:
        #     text_tmp = text_tmp.replace(key, ' ')
        # for key in self.nr_rules:
        #     text_tmp = text_tmp.replace(key, '\n')
        xml_json = BeautifulSoup(text, "lxml")
        json_p = xml_json.find_all("p")
        json_b = xml_json.find_all("blockquote")
        json_tag = json_p + json_b
        list = []

        for tmp_row in json_tag:
            row = tmp_row.text
            # 筛选
            remove_space = row.replace(' ', '')
            if remove_space == '':
                continue
            start_num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
            # 句子开头拼接
            if remove_space.startswith(start_num):
                row = row.lstrip(string.digits).lstrip(".").lstrip("、").lstrip("//").lstrip('。').lstrip(':').lstrip(';')
                # 拆分
                from_key = ['——', '———', '－－', '——']
                for key in from_key:
                    if key in row:
                        row_tmp = row.split(key)
                        list.append([row_tmp[0], row_tmp[-1]])
                        continue
                list.append([row, "NULL"])
                # print("*"+row+"*")
                continue
            elif remove_space.startswith('—') or remove_space.startswith('－－'):
                row = remove_space.strip(string.digits).lstrip("——").lstrip("——")
                if self.sentence != '':
                    self.sentence = self.sentence.strip('\n')      # 去除多余的换行符
                    list.append([self.sentence.lstrip("\n"), row])
                    self.sentence = ""
                    continue
                if len(list) == 0:
                    continue
                list[len(list) - 1][1] = row
                continue  # 句子出处,应该追加到上面那个地方
            else:
                self.sentence = self.sentence + "\n" + row

        return list
    def filter(self, ts):
        list_sentence = self.__filter_sentence(ts)
        if self.sentence != '':
            self.sentence = self.sentence.strip('\n')  # 去除多余的换行符
            list_sentence.append([self.sentence, "NULL"])
            self.sentence = ''
        return list_sentence

if __name__ == '__main__':
    pgs = GJson("https://www.zhihu.com/question/339011506")
    dc = DataClean()
    raw_data = pgs.get_json()
    for index in range(len(raw_data)):
        tmp = dc.filter(raw_data[index][1])
        if tmp == []:
            continue
        print(tmp)
    print(pgs.page_title)