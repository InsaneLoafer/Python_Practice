#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/10 21:00
# @Author   : InsaneLoafer
# @File     : base.py
from selenium import webdriver
import os

class Base:

    def setup(self):
        """
        处理多浏览器
        :return:
        """
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":
            self.driver = webdriver.PhantomJS()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()