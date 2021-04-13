#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/13 22:02
# @Author   : InsaneLoafer
# @File     : login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Exercises.web.podemo.register_page import RegisterPage

class LoginPage:

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        # click register
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        # 进入注册页
        return RegisterPage(self.driver)