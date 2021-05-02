#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/2 21:11
# @Author   : InsaneLoafer
# @File     : test_contact.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    def setup(self):
        caps = {}
        caps ["platformName"] = "Android"
        caps ["deviceName"] = "insane"
        caps ["appPackage"] = "com.tencent.wework"
        caps ["appActivity"] = ".launch.LaunchSplashActivity"
        caps ["noReset"] = "True"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        name = "insane"
        gender = '男'
        phone = '12312312312'
        # 点击【通讯录】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找【添加成员】
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));')
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入姓名
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[text='必填']").send_keys(name)
        # 选择性别
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        elif gender == '女':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        # 输入手机号
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert result == "添加成功"
        # sleep(2)
        # print(self.driver.page_source)
