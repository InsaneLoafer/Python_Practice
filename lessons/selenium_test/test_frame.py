#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/10 22:18
# @Author   : InsaneLoafer
# @File     : test_frame.py
from time import sleep
from lessons.selenium_test.base import Base

class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')    # 切换到iframe中
        drag = self.driver.find_element_by_id("draggable") # 获取drag元素
        print(drag.text)    # 打印元素的文本信息
        """切换到默认的frame
        方法一：切换到父节点
        方法二：切换到默认frame
        """
        self.driver.switch_to.parent_frame() # 切换到父节点
        self.driver.switch_to.default_content() # 切换到默认frame
        print(self.driver.find_element_by_id("submitBTN").text) # 打印点击运行元素的文本
        sleep(3)