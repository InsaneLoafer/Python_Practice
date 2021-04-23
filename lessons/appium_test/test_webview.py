#!/user/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/22 21:38
# @Author   : InsaneLoafer
# @File     : test_browser.py

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestBrowser:

    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platfomVersion': '6.0 ',
            'appPackage': 'io.appium.android.apis',
            'appActivity': 'io.appium.android.apis.ApiDemos',
            # 'browserName': 'Browser',
            'noReset ': True,
            'deviceName ': '127.0.0.1:7555',
            'chromedriverExecutable': '/Users/juanxu/Documents/chromed' # chromedriver路径
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        webview = "WebView"
        print(self.driver.contexts)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                         'scrollable(true).instance(0)).'
                                                         f'scrollIntoView(new UiSelector().text("{webview}").'
                                                         'instance(0));')
        """
        通过Accessbility_id定位针对不同的手机端可能定位不同
        """
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'i has no focus').send_keys("this is a test string")
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'i am a link').click()
        # # 打印页面源码
        # print(self.driver.page_source)
        """
        使用inspect定位，需要先切换上下文
        """
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID, "i_am_a_textbox").send_keys("this is a test string use chrome inspect")
        self.driver.find_element(MobileBy.ID, "i am a link").click()
        print(self.driver.page_source)
