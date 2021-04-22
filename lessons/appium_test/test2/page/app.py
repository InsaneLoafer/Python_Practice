#!/user/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from lessons.appium_test.test2.page.base_page import BasePage
from lessons.appium_test.test2.page.main_page import Main


class App(BasePage):
    def start(self):
        _package = 'com.xueqiu.android'
        _activity = 'com.xueqiu.android.common.MainActivity'
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "Insane"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps['autoGrantPermissions'] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)

        else:
            self._driver.start_activity(_package, _activity) # 如果有_driver，则直接启动app

        return self

    def main(self):
        return Main(self._driver)   # 返回app首页