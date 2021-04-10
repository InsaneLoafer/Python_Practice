#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/9 20:27
# @Author   : InsaneLoafer
# @File     : test_wait.py
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # 使用By.XPATH 或 By.ID 或 By.CSS_SELECTOR
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('selenium')
        # self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        # 在输入框输入selenium
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('selenium')
        # 点击百度一下进行搜索
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)