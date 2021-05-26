#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/29 22:20
# @Author   : ZhangTao
# @File     : tes_time.py
import time

print(time.asctime()) # Tue May 25 14:43:58 2021
print(time.localtime()) # time.struct_time(tm_year=2021, tm_mon=5, tm_mday=25, tm_hour=14, tm_min=43, tm_sec=58, tm_wday=1, tm_yday=145, tm_isdst=0)
print(time.time()) # 1621925038.7708614
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) # 2021-05-25 14:43:58

# 获取两天前的时间
now_time = time.time()
two_day_ago = now_time - 60*60*24*2
time_tuple = time.localtime(two_day_ago) # 将时间戳转换为时间元组
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))