#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/13 22:32
# @Author   : InsaneLoafer
# @File     : addmember.py
from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self, name, account, phonenum):

        # input name
        self.find(By.ID, "username").send_keys(name)
        # input account
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        # input phone
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        # click save，如果页面上相同属性的元素有多个，
        # 那么通过find_element定位到的元素为第一次出现的元素
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_member(self, value):
        # 显示等待
        locator = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(locator=locator)
        # find_elements 方法返回的是元素列表
        titles_total = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            # 获取title列表
            titles = [element.get_attribute("title") for element in elements]
            # 判断名称是否在当前页
            if value in titles:
                return True

            titles_total.extend(titles)

            # 获取页面的起止页码
            page:str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            # 将起止页码分离
            num, total = page.split("/", 1)
            # 如果起止页码相等则跳出循环
            if int(num) == int(total):
                return False
            else:
                # 否则点击下一页
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
        return titles_total
