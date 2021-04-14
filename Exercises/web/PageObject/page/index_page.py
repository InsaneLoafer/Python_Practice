#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/13 22:27
# @Author   : InsaneLoafer
# @File     : index_page.py

from selenium.webdriver.common.by import By
from Exercises.web.PageObject.page.addmember import AddMemberPage
from pageobject.page.base_page import BasePage


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        # 点击添加联系人
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)
