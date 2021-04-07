#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/29 22:20
# @Author   : ZhangTao
# @File     : test_time.py
import time

print(time.asctime())
print(time.localtime())
print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前的时间
now_time = time.time()
two_day_ago = now_time - 60*60*24*2
time_tuple = time.localtime(two_day_ago) # 将时间戳转换为时间元组
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))