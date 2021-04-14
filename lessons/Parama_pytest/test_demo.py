#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/4 15:48
# @Author   : InsaneLoafer
# @File     : test_remote.py
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            """
            由于parametrize 要求传入的参数为list 或 tuple，
            但是我们传入的为字典，所以打印结果为 “test”,所以应修改yaml文件为list
            """
            print(env)
            print(f"测试环境的ip为{env['test']}") # 结果为127.0.0.1


        elif "dev" in env:
            print("这是开发环境")