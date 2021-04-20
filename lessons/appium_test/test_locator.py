#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/19 11:00
# @Author   : InsaneLoafer
# @File     : test_locator.py
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestLocator:
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
        desired_caps['adbExecTimeout'] = 500000
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

    def test_search1(self):
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id ='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
            element_displayed = alibaba_element.get_attribute("displayed")
            if element_displayed == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        action=TouchAction(self.driver)
        # 获取当前屏幕的大小
        width = self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y= y_end).release().perform()

    def test_get_current(self):
        # 点击搜索框
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        # 输入搜索内容
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # 定位到第一个搜索结果
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴").click()
        # 获取股票代码为09988的价格
        price = float(self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        assert price > 200

    def test_myinfo(self):
        """
        1.点击我的，进入个人信息页面
        2.点击登录，进入到登录页
        3.输入用户名、密码
        4.点击登录
        :return:
        """
        self.driver.find_elements_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("账号密码")').click()
        self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("username")
        self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("password")
        self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()

    def test_scroll_find(self):
        self.driver.find_elements_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                         'scrollable(true).instance(0)).'
                                                         'scrollIntoView(new UiSelector().text("黑猫厅长").'
                                                         'instance(0));')

if __name__ == '__main__':
    pytest.main()