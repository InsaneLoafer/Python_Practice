#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/10 21:00
# @Author   : InsaneLoafer
# @File     : base.py
from selenium import webdriver

class Base:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()