#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/13 22:14
# @Author   : InsaneLoafer
# @File     : test_register.py
from Exercises.web.podemo.main_page import MainPage

class TestRegister:
    def setup(self):
        self.main = MainPage()

    def test_register(self):
        # result = self.main.goto_login().goto_register().register()
        result = self.main.goto_register().register()
        assert result
