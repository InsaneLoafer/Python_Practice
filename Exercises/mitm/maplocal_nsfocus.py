#!/user/bin/env python
# -*- coding: utf-8 -*-
from mitmproxy import http

def request(flow: http.HTTPFlow):
    # 发起请求，判断 url 是不是预期值
    if "events" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/genie_events.json") as f:
        # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

    # 发起请求，判断 url 是不是预期值
    if "eventtypesdistr" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/genie_eventtypedistr.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

    # 发起请求，判断 url 是不是预期值
    if "traffic" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/genie_traffic.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )