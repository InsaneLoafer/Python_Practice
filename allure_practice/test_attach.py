#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/4 20:58
# @Author   : InsaneLoafer
# @File     : test_attach.py
import allure
import pytest

def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)

def test_attach_htlm():
    allure.attach("<body>这是一段html body块</body>", 'html测试块', attachment_type=allure.attachment_type.HTML)

# 调用图片要使用file方法
def test_attach_photo():
    allure.attach.file(r"D:\Programs\DevOps\Python_Practice\allure_practice\resource\1.png",
                  name="这是一个图片", attachment_type=allure.attachment_type.PNG)