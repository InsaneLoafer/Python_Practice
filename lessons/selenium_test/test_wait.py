#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/9 20:27
# @Author   : InsaneLoafer
# @File     : test_wait.py
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        # 隐式等待3秒
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        # 直接等待3秒
        sleep(3)
        self.driver.find_element_by_id("su").click()
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, "//*[@class='t c-title-en']")) >= 1
        # until 里面传入一个函数，注意函数后面不能加括号，加了括号就是调用函数
        WebDriverWait(self.driver, 10).until(wait)

        # expected_conditions 为内置判断条件
        expec = expected_conditions.invisibility_of_element((By.XPATH, "//*[@class='t c-title-en']"))
        WebDriverWait(self.driver, 10).until(expec)
        self.driver.find_element_by_class_name("t c-title-en").click()
        print("hello")
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait1(self):
        # 使用By.XPATH 或 By.ID 或 By.CSS_SELECTOR
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('selenium')
        # self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        # 在输入框输入selenium
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('selenium')
        # 点击百度一下进行搜索
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)

