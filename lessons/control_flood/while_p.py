#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/26 20:42
# @Author   : ZhangTao
# @File     : while_p.py
# flag = 0
# while (flag): print('Hello World!')
# print('Pyhon测试开发')
#
# for i in range(10):
#     if i == 5:
#         break #跳出整个循环体
#     print(i) #打印结果为 1,2,3,4
#
# for i in range(10):
#     if i == 5:
#         continue #跳出整个循环体
#     print(i) #打印结果为 1,2,3,4，6,7,8,9。缺少了5

"""
猜数字游戏计算机出一个1~100之间的随机数由人来猜，计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random
number = random.randint(1,100)
while True:
    n = int(input("请输入猜的数字："))
    if n > number:
        print('小一点')
    elif n < number:
        print('大一点')
    elif n == number:
        print('猜对了！')
        break


