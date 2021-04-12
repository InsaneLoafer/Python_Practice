#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/8 12:38
# @Author   : ZhangTao
# @File     : test_hogwarts.py

from selenium import webdriver

class TestHogwards():

    def setup(self):
        self.driver = webdriver.Chrome()
        # 如果没有把driver配置到环境变量，就需要手动添加
        # self.driver = webdriver.Chrome(executable_path="driver path")
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("http://www.testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("健康部落").click()
        ele = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/div[1]/div[1]/div[2]')
        print(ele.text)