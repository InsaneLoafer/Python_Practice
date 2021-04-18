#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/18 21:20
# @Author   : InsaneLoafer
# @File     : demo1.py
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.xueqiu.android '
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
desired_caps['noReset'] = 'true'
desired_caps['dontStopAppOnReset'] = "true"
desired_caps['skipDeviceInitialization'] = "true"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# 隐式等待
driver.implicitly_wait(5)

# 点击搜索框
driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
# 输入搜索内容
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
# 返回上一个页面
driver.back()

driver.quit()
