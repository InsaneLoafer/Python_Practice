#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/11 15:41
# @Author   : InsaneLoafer
# @File     : test_js.py
from time import sleep
from selenium import webdriver


class TestJS:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        """使用js脚本进行元素定位，如果要获取返回一定要加入return"""
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        """滑动到页面最底端"""
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        """点击下一页按钮"""
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(3)
        """获取页面标题和部分性能数据"""
        """方法一：将js命令放在列表中逐个执行"""
        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))

        """方法二：使用分号隔开js命令，在一条语句中执行，但是这时只返回第一个js命令的返回值"""
        # print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_js_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        # 将出发元素赋值
        time_element = "document.getElementById('train_date')"
        # 打印修改前的日期
        print(self.driver.execute_script(f"return {time_element}.value"))
        # 移除元素的readonly属性
        self.driver.execute_script(f"{time_element}.removeAttribute('readonly')")
        # 修改元素的值
        self.driver.execute_script(f"{time_element}.value='2020-12-30'")
        sleep(2)
        # 打印修改的日期
        print(self.driver.execute_script(f"return {time_element}.value"))