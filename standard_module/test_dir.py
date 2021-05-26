#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/29 22:00
# @Author   : ZhangTao
# @File     : test_dir.py
import os

# os.mkdir("testdir")     # 在当前路径创建目录
# print(os.listdir("./")) # 打印当前目录的文件
# os.removedirs("testdir")# 删除文件
# print(os.getcwd())      # 打印当前路径

# 练习：创建b/test.txt，即在当前路径创建目录b并在其下创建文件test.txt
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    with open("b/test.txt", "w") as f:
        f.write("hello, os using")
