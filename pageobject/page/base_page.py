#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/11 21:25
# @Author   : InsaneLoafer
# @File     : base_page.py
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    _base_url = ""
    def __init__(self, driver:WebDriver=None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    # 封装find方法
    def find(self, by, locator):
        return self._driver.find_element(by, locator)