#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/24 10:44
# @Author   : InsaneLoafer
# @File     : rewrite_xueqiu.py

from mitmproxy import http
import json

def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 将响应内容转成字典格式
        data = json.loads(flow.response.content)
        # 修改对应字段的值
        data["data"]["items"][0]["queto"]["name"] = "rewrite_hogwarts"
        # 把修改后的数据转成字符串赋值给原始数据,text是二进制的流格式也就是原始格式
        flow.response.text = json.dumps(data)