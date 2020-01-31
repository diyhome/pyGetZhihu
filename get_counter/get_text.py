#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/31 10:26
# @Author : diyhome
# @Site : https://gitee.com/jingjiangxueyuan_hmqs/
# @File : get_text.py
# @Software: PyCharm
# 参数列表解释:https://luckymrwang.github.io/2019/04/06/知乎-API-v4-整理/

from urllib import request
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        # 日期格式
fp = logging.FileHandler('get_text.log', encoding='utf-8')
fs = logging.StreamHandler()
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用

def get_json(url, offset=0):
    # 截取问题id
    qid = url.split('/')[-1]

    # 安装知乎api v4规则拼接json的url
    json_url = 'https://www.zhihu.com/api/v4/questions/{0}/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question.detail,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[].mark_infos[].url;data[].author.follower_count,badge[].topics&limit=5&offset={1}&platform=desktop&sort_by=default'.format(qid, offset)
    logging.info('json_url: ' + json_url)
    # 伪装浏览器头并且读取json文件
    header = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    head = {}
    head['User-Agent'] = header
    rq = request.Request(json_url, headers=head)
    res = request.urlopen(rq)
    json = res.read().decode('utf-8')
    return json

if __name__ == '__main__':
    json_raw = get_json("https://www.zhihu.com/question/315755986")
    print(json_raw)