#!/user/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TesetTouchAction:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
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
        self.driver.quit()

    def test_touchaction_unlock(self):
        action = TouchAction(self.driver)
        action.press(x=244, y=374).wait(100).move_to(x=711, y=374).wait(100).move_to(x=1198, y=374).\
            wait(100).move_to(x=1198, y=865).wait(100).move_to(x=1198, y=1323).wait(100).release().perform()

