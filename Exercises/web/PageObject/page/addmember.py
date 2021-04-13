#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/13 22:32
# @Author   : InsaneLoafer
# @File     : addmember.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMemberPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def add_member(self, name, accout, phonenum):

        # input name
        self.driver.find_element(By.ID, "username").send_keys(name)
        # input account
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(account)
        # input phone
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phonenum)
        # click save，如果页面上相同属性的元素有多个，
        # 那么通过find_element定位到的元素为第一次出现的元素
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_member(self):
        # find_elements 方法返回的是元素列表
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # 获取title列表
        titles = [element.get_attribute("title") for element in elements]
        return titles
