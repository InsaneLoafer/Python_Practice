#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/24 10:09
# @Author   : InsaneLoafer
# @File     : maplocal_baidu.py
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # 发起请求，判断 url 是不是预期值
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 创造一个 response
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )