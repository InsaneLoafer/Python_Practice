#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/10 12:56
# @Author   : InsaneLoafer
# @File     : test_ActoinChains.py
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_dbl_click = self.driver.find_element(By.CSS_SELECTOR, '[value="dbl click me"]')
        ele_click = self.driver.find_element(By.CSS_SELECTOR, '[value="click me"]')
        ele_right_click = self.driver.find_element(By.CSS_SELECTOR, '[value="right click me"]')
        ele_text = self.driver.find_element(By.CSS_SELECTOR, '[name="t2"]')
        # 实例化ActionChains（）
        action = ActionChains(self.driver)
        # 点击
        action.click(ele_click)
        # 右键
        action.context_click(ele_right_click)
        # 双击
        action.double_click(ele_dbl_click)
        # 执行action
        action.perform()
        print(ele_text.text)
        sleep(4)

    @pytest.mark.skip
    def test_move_to(self):
        """
        光标移动到百度的设置按钮上
        :return:
        """
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        sleep(3)

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id('dragger')
        drop_list = self.driver.find_elements(By.CSS_SELECTOR, '[class="item"]')
        action = ActionChains(self.driver)
        # 将方块移动到每个item中并释放
        for drop_ele in drop_list:
            """方法一：使用drag_and_drop 方法"""
            # sleep(1)
            # action.drag_and_drop(drag_ele, drop_ele).perform()

            """方法二：先进行点击并hold住，再释放"""
            # action.click_and_hold(drag_ele).release(drop_ele).perform()

            """方法三：先进行点击并hold住，再移动到目的元素上，最后释放"""
            action.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH, '//*[@type="textbox"][1]')
        ele.click() # 首先要将光标移动到输入框
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)       # 首先输入username，并等待一秒
        action.send_keys(Keys.SPACE).pause(1)       # 然后输入空格
        action.send_keys("Tom").pause(1)            # 然后输入Tom
        action.send_keys(Keys.BACK_SPACE).pause(1).perform() # 最后删除一个字符
        sleep(3)


if __name__ == '__main__':
    pytest.main(['-v','-s','test_ActionChains.py'])
