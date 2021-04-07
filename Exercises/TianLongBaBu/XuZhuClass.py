#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/3 23:12
# @Author   : InsaneLoafer
# @File     : XuZhuClass.py
"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
from Exercises.TianLongBaBu.TongLaoClass import TongLao

# 定义虚竹类，并继承TongLao类
class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")

if __name__ == '__main__':
    xuzhu = XuZhu(200, 20)
    xuzhu.see_people(name="DCQ")
    xuzhu.fight_zms(500,50)
    xuzhu.read()


