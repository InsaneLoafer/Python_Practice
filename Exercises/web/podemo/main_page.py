#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/13 21:57
# @Author   : InsaneLoafer
# @File     : main_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from Exercises.web.podemo.login_page import LoginPage
from Exercises.web.podemo.register_page import RegisterPage

# 主页
class MainPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        # click login
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # 进入登录页面
        return LoginPage(self.driver)

    def goto_register(self):
        # click register
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # 进入注册页
        return RegisterPage(self.driver)