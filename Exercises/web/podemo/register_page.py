#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/13 22:07
# @Author   : InsaneLoafer
# @File     : register_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class RegisterPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        # input company name
        self.driver.find_element(By.ID, "corp_name").send_keys("corpname")
        # input phone number
        self.driver.find_element(By.ID, "register_tel").send_keys("12312312311")
        # click register
        self.driver.find_element(By.ID, "submit_btn").click()

        return True
