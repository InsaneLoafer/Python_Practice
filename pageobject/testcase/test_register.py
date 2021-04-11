#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/11 21:45
# @Author   : InsaneLoafer
# @File     : test_register.py
from pageobject.page.main import Main

class TestRegister:
    def setup(self):
        self.main = Main()

    def test_main_to_register(self):
        """进入首页，点击立即注册进行注册"""
        assert "企业信息" == self.main.goto_register().register()

    def test_login_to_register(self):
        """进入首页，点击登录，再点击登录页的立即注册"""
        assert "企业信息" == self.main.goto_login().goto_register().register()