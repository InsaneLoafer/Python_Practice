#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/8 20:37
# @Author   : InsaneLoafer
# @File     : test_encode.py

import pytest

@pytest.mark.parametrize('name', ['哈利','赫敏'])
def test_chinese(name):
    print(name)