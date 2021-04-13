#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/13 22:27
# @Author   : InsaneLoafer
# @File     : index_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Exercises.web.PageObject.page.addmember import AddMemberPage


class IndexPage:

    def __init__(self):
        # 复用浏览器
        option = Options()
        option.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def goto_add_member(self):
        # 点击添加联系人
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)
