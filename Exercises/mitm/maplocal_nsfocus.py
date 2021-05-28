#!/user/bin/env python
# -*- coding: utf-8 -*-
from mitmproxy import http
import pystache


# 执行：`mitmdump -p 8999 -s maplocal_nsfocus.py --ssl-insecure`
_adbos_ip = "10.66.253.120"
_env_id = [2, 3, 8, 10] # ads/nta——2； Genie——3； UMC——8； ATIC——10
_device = [["ads", "nta"], "genieatm", ["umc_probe", "umc_guard"], ["atic_detection", "atic_mitigation"]]
with open("data/events.mustache", "r", encoding="utf-8") as e:
    event = pystache.render(
        e,
        {
            "adbos_ip": _adbos_ip,
            "env_id": _env_id[1],
            "device": _device[1]
        }
    )

def request(flow: http.HTTPFlow):
    # 发起请求，判断 url 是不是预期值
    if "events" in flow.request.pretty_url:
        # 创造一个 response
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            event,  # (optional) content
            {"Content-Type": "application/json"}  # (optional) headers
        )

    # 发起请求，判断 url 是不是预期值
    if "eventtypesdistr" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/eventtypedistr.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

    # 发起请求，判断 url 是不是预期值
    if "traffic" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/traffic.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

    # 发起请求，判断 url 是不是预期值
    if "srctopn" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/srctopn.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

    # 发起请求，判断 url 是不是预期值
    if "/topn/?chart=bar&unit=bps&sortby=In" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/topn.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

    # 发起请求，判断 url 是不是预期值
    if "eventdistr" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/eventdistr.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

    # 发起请求，判断 url 是不是预期值
    if "srctopngeodist" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/srctopngeodist.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

    # 发起请求，判断 url 是不是预期值
    if "abnormaltopn" in flow.request.pretty_url:
        # 打开一个保存在本地的文件
        with open("data/adnormaltopn.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )
