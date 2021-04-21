#!/user/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast():
    def setup( self) :
        desire = {
            'platformName': 'android',
            'platformVersion': '6.0 ',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'io.appium.android.apis',
            'appActivity': 'lo.appium.android.apis.view.PopupMenu1',
            'antomationName': 'uiautomator2' # 默认使用此引擎
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire)
        self.driver.implicitly_wait(5)

    def teardown(self) :
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        # 打印当前页面的Dom树
        print(self.driver.page_source)
        """
        打印toast文本有以下两个方法
        """
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, 'Clicked popup')]").text)