#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/10 14:27
# @Author   : InsaneLoafer
# @File     : test_TouchAction.py
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions

class TestTouchAction:

    def setup(self):
        """当使用TouchAction时会报错不是w3c的标准命令，可以使用以下解决"""
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_scroll_bottom(self):
        self.driver.get("http://www.baidu.com")
        ele_input = self.driver.find_element_by_id('kw')
        ele_input.send_keys('selenium测试')   # 输入框中输入内容
        ele_search = self.driver.find_element_by_id('su')
        action = TouchActions(self.driver)
        action.tap(ele_search).perform()  # 点击百度一下进行搜索
        action.scroll_from_element(ele_input, 0, 10000).perform()   # 完成页面滑动
        sleep(2)
        self.driver.find_element_by_link_text("下一页 >").click()  # 滑动到最下面点击下一页
        sleep(1)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_TouchAction.py'])