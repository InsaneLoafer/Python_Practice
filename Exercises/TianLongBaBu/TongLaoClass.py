#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/3 22:54
# @Author   : InsaneLoafer
# @File     : TongLaoClass.py
"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”。
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
"""

# 定义童姥类
class TongLao:
    # 使用构造方法定义实例变量 血量和武力值
    def __init__(self, tonglao_hp, tonglao_power):
        self.tonglao_hp = tonglao_hp
        self.tonglao_power = tonglao_power

    # 定义see_people 方法
    def see_people(self, name):
        # 判断name的值
        name: str = input("请输入名字：")
        if name == 'WYZ':
            print("师弟！！！")

        elif name == "LQS":
            print("师弟是我的！")

        elif name == "DCQ":
            print("叛徒！我杀了你！")

        # 如果输入其他的字符，则进行提示并重新调用see_people
        else:
            print("请输入：WYZ 或 LQS 或 DCQ")
            self.see_people(name)

    # fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
    def fight_zms(self, enemy_hp, enemy_power):
        self.tonglao_hp /= 2
        self.tonglao_power *= 10
        self.tonglao_hp -= enemy_power
        enemy_hp -= self.tonglao_power
        # 判断血量
        if self.tonglao_hp > enemy_hp:
            print(f'童姥的血量是{self.tonglao_hp}，童姥的武力值是{self.tonglao_power}')
            print(f'敌人的血量是{enemy_hp}')
            print('童姥获胜')

        elif self.tonglao_hp <= enemy_hp:
            print(f'童姥的血量是{self.tonglao_hp}，童姥的武力值是{self.tonglao_power}')
            print(f'敌人的血量是{enemy_hp}')
            print('敌人获胜')

if __name__ == '__main__':

    tonglao= TongLao(200, 100)
    tonglao.see_people(12)
    tonglao.fight_zms(300, 50)