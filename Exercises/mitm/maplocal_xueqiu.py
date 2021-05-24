#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/24 10:23
# @Author   : InsaneLoafer
# @File     : maplocal_xueqiu.py
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # 发起请求，判断 url 是不是预期值
    if "quote.json" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("path/quote.json") as f:
        # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )