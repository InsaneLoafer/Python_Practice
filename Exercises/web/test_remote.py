#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/12 20:47
# @Author   : InsaneLoafer
# @File     : test_remote.py
import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestWX:
    def setup(self):
        """复用浏览器"""
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
        # 获取当前页面的cookies
        cookies = self.driver.get_cookies()
        print(cookies)
        # 将每个cookie放在当前的页面上
        for cookie in cookies:
            """add_cookie方法传入字典类型，且关键字的值不能为float类型，所以应将cookie中的到期时间去掉"""
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.refresh() # 刷新页面

    def test_shelve(self):
        """shelve 是Python自带的对象持久化存储小型数据库
        以key：value形式存储
        """
        db = shelve.open("cookies") # 生成cookies.db 文件
        # db["cookie"] = self.driver.get_cookies() # 获取cookie后将此代码注释
        cookies = db["cookie"]
        db.close() # 关闭数据库

        # 打开新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 加入cookie
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.refresh()  # 刷新页面

    def test_import_contacts(self):
        # shelve 模块， python 自带的对象持久化存储
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        # 刷新当前页面，获取登录状态
        self.driver.refresh()
        # 点击【导入联系人】
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传文件，选择文件的完整路径上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "/Users/juanxu/Downloads/mydata.xlsx")
        # 断言上传文件名，与实际文件名一致
        result = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "mydata.xlsx" == result
        sleep(5)
