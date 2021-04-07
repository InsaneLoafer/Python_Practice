#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/2 21:56
# @Author   : ZhangTao
# @File     : test_a.py
# content of test_sample.py
import pytest

def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (1,2),(3,4),(20,20)
])
def test_answer(a,b):
    assert func(a) == b

def test_answer1():
    assert func(4) == 5

@pytest.fixture()   # 可以将函数的值传给另一个函数执行前
def login():
    print("登录操作")
    username = 'Michael'
    return username

class TestDemo:
    def test_a(self, login):    # 在执行test_a前执行login()函数
        print(f"a, username = {login}") # 调用login()返回的值

    def test_b(self):
        print("b")

# 利用Python的入口函数使用Python解释器来运行
if __name__ == '__main__':
    # 运行test_a.py文件下的TestDemo测试类，-v 可以详细打印出日志
    pytest.main(["test_a.py::TestDemo",'-v'])


