#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/11 19:26
# @Author   : InsaneLoafer
# @File     : test_alert.py
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestAlert:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult") # 切换到iframe中
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform() # 将元素1拖拽到元素2
        sleep(2)
        alert = self.driver.switch_to.alert
        print(alert.text)   # 打印弹窗信息
        alert.accept()    # 点击弹框的确定
        self.driver.switch_to.default_content() # 切换到默认frame中
        self.driver.find_element_by_id("submitBTN").click()

