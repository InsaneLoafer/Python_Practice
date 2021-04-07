#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/3 20:03
# @Author   : InsaneLoafer
# @File     : python_oop.py

# 面向对象
class House:
    # 静态属性-> 类变量，类之中方法之外，在类中的方法调用需要加上 self.
    door = 'red'
    floor = 'white'

    # 构造函数，定义实例变量，在类实例化的时候就执行
    """
    Python中规定无论是构造方法还是实例方法，都必须至少包含一个参数，
    参数名称self只是程序员编码的习惯，其实也可以定义为其他名称，这样
    每个类对象只能调用自己的类变量和类方法。
    self指代的其实是 north_house 和 china_house，即对象本身。
    """
    def __init__(self):
        # 在方法中调用类变量需要加上self.
        print(self.door)

        # 实例变量：类当中，方法当中，以“self.变量名”方式定义
        self.kitchen = "cook"


    # 动态方法
    def sleep(self):
        # 普通变量：在类当中，在方法当中，并且前面没有 .self，只能在当前方法中调用
        bed = "席梦思"
        self.table = "桌上可以放东西"
        print(f'在房子里可以在{bed}上睡觉')

    def cook(self):
        # 调用实例变量
        print(self.kitchen)

        # 调用非构造方法的实例变量
        print(self.table)
        print('在房子里可以做饭')

# 把类实例化
# 北欧风房子
north_house = House()
# 中式风房子
china_house = House()

"""
在cook中调用了sleep中的table，
执行时就要先调用sleep，不然会报错：没有 table 这个对象
"""
north_house.sleep()
north_house.cook()

# 调用类的属性
print(House.door)   # 结果为red
# 修改类属性
House.door = 'white'
print(House.door)   # 结果为white
# 实例对象调用类的属性
print(north_house.door) # 修改类属性前为red，修改后为white
# 修改对象属性，作用域只限于本对象
north_house.door = 'black'
print(north_house)  # 结果为black
print(House.door)   # 结果为red
print(china_house.door) # 结果为red

print(north_house.sleep())  # 结果为“在房子里可以在席梦思上睡觉”
