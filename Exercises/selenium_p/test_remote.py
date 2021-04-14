#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/12 12:48
# @Author   : ZhangTao
# @File     : test_remote.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        """
        复用浏览器
        """
        option = Options()
        """
        注意：
        1. 浏览器要提前打开
        2. 9222端口要与命令行启动的端口一致
        """
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wx(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, 'menu_contacts').click() # 点击通讯录

    def test_cookie(self):
        # 获取当前页面的cookie
        cookies = self.driver.get_cookies()
        print(cookies)
        # 添加cookie到当前页面
        """
        add_cookie() 里面的cookie过期时间不支持float类型，所以可以将expiry字段去掉再执行
        """
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        self.driver.refresh() # 刷新一次