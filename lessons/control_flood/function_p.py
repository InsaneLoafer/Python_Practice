#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/26 21:09
# @Author   : ZhangTao
# @File     : function_p.py

# 函数的定义
def func1(a,b,c):
    """
    函数func1的作用
    :param a:参数a是用来打印的
    :param b:
    :param c:
    :return:
    """
    # 使用Tab键进行缩进
    # ctrl+d可以复制一行
    print("这是一个函数")
    print("这是一个参数a",a)
    print("这是一个参数b",b)
    print("这是一个参数c",c)
    return a

# 函数的调用
func1(1,2,3)
# 如果有一个参数未指定，那么后面的参数都不能指定
func1(2, 4, 5)
# 打印函数的返回值
print(func1(3,2,1)) # 结果为3

# 关键字参数
def func2(a,b,c,d):
    print("参数a的值为：",a)
    print("参数b的值为：",b)
    print("参数c的值为：",c)
    print("参数d的值为：",d)
func2(b=2,c=3,a=10,d=4)

# 关键字参数
def func2(a,b,c,*,d): # 在d前面加一个*,则d必须为关键字参数
    print("参数a的值为：",a)
    print("参数b的值为：",b)
    print("参数c的值为：",c)
    print("参数d的值为：",d)
func2(2,3,10,d=4)

# lambda表达式
func3 = lambda x: x*2
print(func3(3)) # 结果为6
# 等同于
def func4(x):
    return x*2
print(func4(3))

# 定义多个参数
fun5 = lambda x,y:x+y
print(fun5(2,4))
