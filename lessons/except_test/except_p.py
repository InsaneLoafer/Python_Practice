#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/28 21:23
# @Author   : ZhangTao
# @File     : except_p.py

# try:
#     num1 = int(input("输入一个除数："))
#     num2 = int(input("输入一个被除数："))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("被除数不能为0")
# except ValueError:
#     print("输入的需要是数值型整数")
# except:  # 捕获所有异常
#     print("这是一个通用型异常")
# else:
#     print("程序没有发生异常")
# finally:
#     print("无论发没发生异常，都执行")
#
# # 主动抛出异常
# x = 10
# if x > 5:
#     raise Exception("这是抛出的异常")

# 自定义异常
class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

raise MyException("value1", "value2")