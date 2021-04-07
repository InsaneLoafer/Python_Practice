#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/4 19:41
# @Author   : InsaneLoafer
# @File     : test_link_issue.py
import allure

@allure.link("www.baidu.com", name="百度一下")
def test_with_link():
    print("这是一条加了链接的测试")
    pass

# 测试用例链接
TST_CASE_LINK ='https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.testcase(TST_CASE_LINK, '登录用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接，链接到测试用例里面")
    pass

# 测试bug链接，前面为bugID
"""
在运行时加入bug链接： --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
中括号里面就会传bugID
"""
@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    pass
