#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/16 21:29
# @Author   : InsaneLoafer
# @File     : demo.py

from appium import webdriver

desire_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noRest": True  # 不对应用进行重置，保留app之前的设置

}
"""
appium默认监听本地4723端口
"""
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/"
                                   "android.widget.LinearLayout/android.widget.FrameLayout/"
                                   "android.view.ViewGroup/android.widget.FrameLayout/android"
                                   ".widget.LinearLayout/android.widget.RelativeLayout/android."
                                   "widget.FrameLayout/android.widget.LinearLayout/androidx."
                                   "recyclerview.widget.RecyclerView/android.widget.Relative"
                                   "Layout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el3.click()

