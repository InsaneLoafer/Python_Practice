#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/22 21:38
# @Author   : InsaneLoafer
# @File     : test_browser.py
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:

    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platfomVersion': '6.0 ',
            'browserName': 'Browser',
            'noReset ': True,
            'deviceName ': '127.0.0.1:7555',
            # 'chromedriverExecutable ' : '/Users/juanxu/Documents/chromed`
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        search_locator = (By.ID, "index-bn")
        # 显示等待
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()

