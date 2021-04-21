#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/21 21:45
# @Author   : InsaneLoafer
# @File     : test_param.py
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestParam:
    def setup(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.main.view.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = "true"
        """当要输入中文时需要以下两个参数"""
        desired_caps['unicodeKeyBoard']='true'
        desired_caps['resetKeyBoard']='true'
        # # 超时时间
        # desired_caps['adbExecTimeout'] = 500000
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click() # 点击取消
        pass

    @pytest.mark.parametrize('searchkey, type, expected_price', [
        ('alibaba', 'BABA', 180),
        ('xiaomi', '01810', 10)
    ])
    def test_get_search(self, searchkey, type, expected_price):
        """
        1.打开雪球应用
        2.点击搜索框
        3.输入搜索词“alibaba”、“小米”
        4.点击第一个搜索结果
        5.判断股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        current_price = self.driver.find_element\
            (MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert_that(current_price, close_to(expected_price, expected_price*0.1))
