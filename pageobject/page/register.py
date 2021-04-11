#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/11 21:35
# @Author   : InsaneLoafer
# @File     : register.py
from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage

class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("username")
        self.find(By.ID, "manager_name").send_keys("managername")
        return self.find(By.CSS_SELECTOR, ".register_simple_sec_title").text