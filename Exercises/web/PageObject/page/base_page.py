#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/14 12:32
# @Author   : InsaneLoafer
# @File     : base_page.py

"""
基类，用来完成一些初始化操作，存放最基本的方法，比如实例化driver、find等
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""
    def __init__(self, driver:WebDriver = None):
        if driver == None:
            # 复用浏览器
            option = Options()
            option.debugger_address="127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

        else:
            self.driver = driver

        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    # 封装显示等待
    def wait_for_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))