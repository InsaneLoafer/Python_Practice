#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/9 12:30
# @Author   : ZhangTao
# @File     : test_remote.py

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID, 'kw').send_keys('Selenium')
        self.driver.find_element(By.ID, 'su').click()