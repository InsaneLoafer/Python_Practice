#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/8 20:32
# @Author   : InsaneLoafer
# @File     : __init__.py.py
from typing import List
import pytest


def pytest_collection_modifyitems(session, config, items:List):
    # 修改编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

    # 修改用例执行顺序，其中 items 就是所有用例列表
    items.reverse()  # 倒序执行