#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/4 15:04
# @Author   : InsaneLoafer
# @File     : param_p.py
import pytest

# 参数使用string
import yaml


@pytest.mark.parametrize("a,b", [(10,20), (30,40)])
def test_param(a, b):
    print(a+b)

# 参数使用list
@pytest.mark.parametrize(["a","b"], [(10,20), (30,40)])
def test_param(a, b):
    print(a+b)

# 参数使用tuple
@pytest.mark.parametrize(("a","b"), [(10,20), (30,40)])
def test_param(a, b):
    print(a+b)

class TestData:
    @pytest.mark.parametrize("a,b",yaml.safe_load(open("data.yaml")))
    def test_data(self, a, b):
        print(a+b)
