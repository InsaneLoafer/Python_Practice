#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/28 20:24
# @Author   : ZhangTao
# @File     : test_file.py
f = open('data.txt')
print(f.readable())
# print(f.readlines()) #以列表形式读
print(f.readline()) #逐行读
print(f.readline())
print(f.readline())
f.close()

# 不用再单独关闭文件，可以将文件打开后操作完毕后自动关闭
with open('data.txt') as f:
    print(f.readlines())

# 标准的读数据方法
with open('data.txt') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break