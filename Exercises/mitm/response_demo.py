#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/24 10:37
# @Author   : InsaneLoafer
# @File     : response_demo.py
from pprint import pprint
from mitmproxy import http


def response(flow: http.HTTPFlow):
    pprint(flow.response.content)