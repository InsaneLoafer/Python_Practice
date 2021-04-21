#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/21 21:35
# @Author   : InsaneLoafer
# @File     : test_assert.py

from hamcrest import *

def test_assert():
    a = 10
    b = 20
    assert a > b  # 第一条断言失败则不会运行后面的断言
    assert "h" in "this"


def test_hamcrest():
    assert_that(10, equal_to(10), "这是一个提示") # 等于
    assert_that("contains some string", contains_string("string"))  # 包含
    assert_that(13, close_to(10, 2), "应在范围10-12内") # 在10的上下2浮动，范围为8-12
