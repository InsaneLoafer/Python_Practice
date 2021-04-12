#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/10 20:58
# @Author   : InsaneLoafer
# @File     : test_window.py
from time import sleep
from lessons.selenium_test.base import Base

class TestWindow(Base):

    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click() # 点击登录
        self.driver.find_element_by_link_text("立即注册").click()   # 点击立即注册

        """此时弹出新的注册窗口，需要跳转到新窗口"""
        cur_handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        """方法一：判断所有的窗口，如果窗口标题包含注册就跳转"""
        for handle in handles:
            if "注册" in handle.title():
                self.driver.switch_to_window(handle)
        """方法二：直接跳转到最新的窗口，即最后一个窗口"""
        # self.driver.switch_to_window(handles[-1])

        """输入用户名和和密码"""
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_4__userNameTip').send_keys('password')
        sleep(2)

        """跳转到百度首页，输入账号密码"""
        self.driver.switch_to_window(cur_handle)
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()  # 点击用户名登录
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        sleep(2)