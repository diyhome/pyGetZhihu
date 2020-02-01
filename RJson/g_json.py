#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/1 10:23
# @Author : diyhome
# @Site : https://gitee.com/jingjiangxueyuan_hmqs/
# @File : rjson.py
# @Software: PyCharm
from urllib import request
import logging
import json

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        # 日期格式
fp = logging.FileHandler('pyzhihu.log', encoding='utf-8')
fs = logging.StreamHandler()
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用

class GJson:
    page_title = "null"
    def __init__(self, url):
        self.url = url

    def __data_filter(self, raw_data):
        # 如果回答中包含了图片,直接舍弃
        # if "img" in raw_data['content']:
        #     return
        data_tmp = []
        data_tmp.append(raw_data['author']['name'])
        data_tmp.append(raw_data['content'])
        data_tmp.append(raw_data['voteup_count'])
        return data_tmp
    def get_json(self, offset = 5):
        # 截取问题id
        qid = self.url.split('/')[-1]

        data_res = []
        # 按照知乎api v4规则拼接json的url
        json_url = 'https://www.zhihu.com/api/v4/questions/{0}/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question.detail,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[].mark_infos[].url;data[].author.follower_count,badge[].topics&limit=5&offset={1}&platform=desktop&sort_by=default'.format(
            qid, offset)

        # 伪装浏览器头并且读取json文件
        header = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
        head = {}
        head['User-Agent'] = header
        while True:
            logging.info('json_url: ' + json_url)
            rq = request.Request(json_url, headers=head)
            res = request.urlopen(rq)
            json_raw = res.read().decode('utf-8')
            data = json.loads(json_raw)
            # 标题获取
            self.page_title = data['data'][0]['question']['title']
            tmp = []
            for index in range(len(data['data'])):
                tmp = self.__data_filter(data['data'][index])
                data_res.append(tmp)
            logging.debug("paging.is_end:" + str(data['paging']['is_end']))
            # 判断json读取结束:因为json自带一个属性is_end
            if data['paging']['is_end']:
                break
            json_url = data['paging']['next']
        return data_res