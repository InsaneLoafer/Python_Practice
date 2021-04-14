#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/13 22:40
# @Author   : InsaneLoafer
# @File     : test_contact.py
from Exercises.web.PageObject.page.index_page import IndexPage

class TestContact:

    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        name = "aa_0"
        account = "124"
        phonenum = "13911111111"

        addmemberpage = self.index.goto_add_member()
        addmemberpage.add_member(name, account, phonenum)
        result = addmemberpage.get_member(name)
        assert result