#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/28 20:57
# @Author   : ZhangTao
# @File     : test_json.py

import json
data = {
    'name':['jerry','nickname'],
    'age':18,
    'gender':'male'
}
# 转化为string类型
data1 = json.dumps((data))
print(type(data))
print(data1,type(data1))

# 转换为dict类型
data2 = json.loads(data1)
print(type(data2))

