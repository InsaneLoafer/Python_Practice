#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/7 20:40
# @Author   : InsaneLoafer
# @File     : test_chinese.py
import pytest

@pytest.mark.parametrize('name', ['哈利','赫敏'])
def test_chinese(name):
    print(name)

def test_login():
    print("login")

def test_login_fail():
    print("login fail")
    assert False

def test_search():
    print("search")

# 将在conftest中定义的fixture函数传过来
def test_env(cmdoption):
    env, datas = cmdoption
    print(datas)
    host = datas['env']['host']
    port = datas['env']['port']
    url = str(host) + ":" + str(port)
    print(url)