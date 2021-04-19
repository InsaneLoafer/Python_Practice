#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/19 11:00
# @Author   : InsaneLoafer
# @File     : test_locator.py
import pytest
from appium import webdriver

class TestLocator:
    def setup(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android '
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = "true"
        """当要输入中文时需要以下两个参数"""
        desired_caps['unicodeKeyBoard']='true'
        desired_caps['resetKeyBoard']='true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.back()
        self.driver.quit()

    def test_search(self):
        """
        1.打开雪球app
        2．点击搜索输入框
        3．向搜索输入框里面输入"阿里巴巴"
        4。在搜索结果里面选择"阿里巴巴"，然后进行点击
        5．获取阿里巴巴的股价，并判断这只股价的价格 > 200
        """

        # 点击搜索框
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        # 输入搜索内容
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # 定位到第一个搜索结果
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴").click()
        # 获取到阿里巴巴股票的价格
        current_price = float(self.driver.find_element_by_id("com. xueqiu.android:id/current_price").text)
        assert current_price > 200

if __name__ == '__main__':
    pytest.main()