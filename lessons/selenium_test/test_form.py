#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/10 14:49
# @Author   : InsaneLoafer
# @File     : test_form.py
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id('user_login').send_keys("123")   # 输入用户名
        self.driver.find_element_by_id('user_password').send_keys('password') # 输入密码
        self.driver.find_element_by_id('user_remember_me').click()  # 点击记住登录状态
        self.driver.find_element(By.XPATH, '//*[@name="commit"]').click() # 点击登录即提交表单按钮
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_form.py'])