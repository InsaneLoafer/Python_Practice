#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/11 19:02
# @Author   : InsaneLoafer
# @File     : test_fileupload.py
from time import sleep
from selenium import webdriver

class TestFile:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_id("sttb").click()
        self.driver.find_element_by_id("uploadImg").send_keys("1.png")
        sleep(2)