#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/3 15:17
# @Author   : InsaneLoafer
# @File     : game_round1.py
"""
一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法:
   - my_final_hp = my_hp - enemy_power
   - enemy_final_hp = enemy_hp - my_power
   - 两个hp进行对比，血量剩余多的人获胜
"""
import random


def fight(enemy_hp, enemy_power):
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    print(f'敌人的血量为：{enemy_hp}')
    print(f'敌人的攻击力为：{enemy_power}')
    # 加入循环，使游戏进行多轮
    turn = 1
    while True:
        my_hp -= enemy_power
        enemy_hp -= my_power

        # 判断谁的血量小于0
        if my_hp <= 0:
            print()
            print(f"________第{turn}轮__________")
            print(f"我的血量剩余为：{my_hp}，敌人的血量为：{enemy_hp}")
            print("我输了！")
            break
        elif enemy_hp <= 0:
            print()
            print(f"________第{turn}轮__________")
            print(f"我的血量剩余为：{my_hp}，敌人的血量为：{enemy_hp}")
            print("我赢了！")
            break
        turn += 1


# Python入口函数
if __name__ == '__main__':
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1011)]
    # print(hp)
    # print(type(hp))
    # 让敌人的hp从hp列表中随机挑选一个值
    enemy_hp = random.choice(hp)
    # print(f'敌人的血量为：{enemy_hp}')
    # 随机生成敌人的攻击力
    enemy_power = random.randint(100, 201)
    # print(f'敌人的攻击力为：{enemy_power}')

    # 调用函数，传入敌人的hp和power
    fight(enemy_hp, enemy_power)
