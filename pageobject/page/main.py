#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/11 21:23
# @Author   : InsaneLoafer
# @File     : main.py
from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage
from pageobject.page.login import Login
from pageobject.page.register import Register

class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click() # 点击注册按钮
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click() # 点击企业登录
        return Login(self._driver)