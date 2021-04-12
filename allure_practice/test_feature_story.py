#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/4 19:03
# @Author   : InsaneLoafer
# @File     : test_feature_story.py

import pytest
import allure

# 标识整个模块都用来进行登录
@allure.feature('登录模块')
class TestLogin():

    @pytest.mark.run(order=1)
    @allure.story('登录成功')
    def test_login_success(self):
        print("这是登录：测试用例，登陆成功")
        pass

    @pytest.mark.run(order=2)
    @allure.story('登录失败')
    def test_login_fail(self):
        print("这是登录：测试用例，登陆失败")
        pass

    @allure.story('用户名缺失')
    def test_login_lostname(self):
        print("用户名缺失")
        pass

    @pytest.mark.run(order=-1)
    @allure.story('密码缺失')
    def test_login_lostsec(self):

        # 对一些关键步骤进行标记
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert "1" == 1
            print("登录失败")
        pass

    @pytest.mark.run(order=0)
    @allure.story("登录失败")
    def test_login_failure(self):
        pass


