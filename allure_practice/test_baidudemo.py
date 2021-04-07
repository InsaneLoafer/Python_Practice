#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/4 21:36
# @Author   : InsaneLoafer
# @File     : test_baidudemo.py
import time
import allure
import pytest
from selenium import webdriver

@allure.testcase("http://www/github.com", "测试用例地址")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data):

    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.maximize_window() # 浏览器最大化
        driver.get("http://www.baidu.com")

    with allure.step("输入搜索词"):
        driver.find_element_by_id("kw").send_keys(test_data)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./resource/b.png")
        allure.attach.file("./resource/b.png", attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body>首页</body>','Attach with HTML type',allure.attachment_type.HTML)

    with allure.step("关闭浏览器"):
        driver.quit()