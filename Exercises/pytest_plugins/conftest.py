#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/7 20:47
# @Author   : InsaneLoafer
# @File     : conftest.py

from typing import List
import pytest
import yaml


# def pytest_collection_modifyitems(session, config, items:List):
#     # 修改编码
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
#
#         # 如果login在测试用例路径中，则对其打标签
#         if "login" in item.nodeid:
#             item.add_marker(pytest.mark.login)
#
#     # 修改用例执行顺序，其中 items 就是所有用例列表
#     items.reverse()  # 倒序执行

# 添加一个命令行参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts") #group将下面所有的option都展示在这个group下。
    mygroup.addoption("--env",            #注册一个命令行选项
                    default='test',     #参数的默认值
                    dest='env'          ,#存储的变量
                    help='set your run env' #帮助提示参数的描述信息
                    )

# 定义fixture从而获取addoption里面函数
@pytest.fixture(scope='session')
def cmdoption(request):
    env = request.config.getoption("--env", default='test')

    if env == 'test':
        print("这是测试环境")
        datapath = "./datas/test/datas.yml"

    elif env == 'dev':
        print("这是开发环境")
        datapath = "./datas/dev/datas.yml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return env, datas