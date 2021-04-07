#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/29 22:37
# @Author   : ZhangTao
# @File     : test_urllib.py
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
print(response.status) # 返回状态码
print(response.read())  # 响应信息
print(response.heanders)    # 头部信息