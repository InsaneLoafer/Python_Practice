#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/3 21:09
# @Author   : InsaneLoafer
# @File     : game_oop.py

class Game:

    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199


    def fight(self):

        # 加入循环，使游戏进行多轮
        turn = 1
        while True:
            self.my_hp -= self.enemy_power
            self.enemy_hp -= self.my_power

            # 判断谁的血量小于0
            if self.my_hp <= 0:
                print()
                print(f"________第{turn}轮__________")
                print(f"我的血量剩余为：{self.my_hp}，敌人的血量为：{self.enemy_hp}")
                print("我输了！")
                break
            elif self.enemy_hp <= 0:
                print()
                print(f"________第{turn}轮__________")
                print(f"我的血量剩余为：{self.my_hp}，敌人的血量为：{self.enemy_hp}")
                print("我赢了！")
                break
            turn += 1

    # 在父类定义休息的方法
    def rest(self, time_num):
        print(f'太累了，休息{time_num}分钟')

class HouYi(Game):
    # 定义护甲属性
    def __init__(self, defense, my_hp, enemy_hp):
        self.defense = defense
        # 通过继承调用父类的构造方法，拿到父类的属性
        super().__init__(my_hp, enemy_hp)


    # 改造fight方法
    def fight(self):
        # 加入循环，使游戏进行多轮
        turn = 1
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp -= self.my_power

            # 判断谁的血量小于0
            if self.my_hp <= 0:
                print()
                print(f"________第{turn}轮__________")
                print(f"我的血量剩余为：{self.my_hp}，敌人的血量为：{self.enemy_hp}")
                print("我输了！")
                break
            elif self.enemy_hp <= 0:
                print()
                print(f"________第{turn}轮__________")
                print(f"我的血量剩余为：{self.my_hp}，敌人的血量为：{self.enemy_hp}")
                print("我赢了！")
                break
            turn += 1

houyi = HouYi(20, 100, 20)
houyi.fight()
# 子类的对象调用父类的方法
houyi.rest(3)