#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/24 10:02
# @Author   : InsaneLoafer
# @File     : request_demo.py

from mitmproxy import http


def request(flow: http.HTTPFlow):
    flow.request.headers["myheader"] = "insane"
    print(flow.request.headers)