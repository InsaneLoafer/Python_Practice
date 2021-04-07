#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/3 20:44
# @Author   : InsaneLoafer
# @File     : bicycle.py
# - 写一个Bicycle(自行车)类，有run(骑行)方法，调用时显示骑行里程km(骑行里程为传入的数字):
# - 再写一个电动自行车类EBicycle继承自Bicycle，添加电池电量valume属性通过，参数传入，同时有两个方法:
#   - 1. fill_charge(vol)用来充电, vol为电量
#   - 2. run(km)方法用于骑行，每骑行10km消耗电量1度，当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果

# 自行车类
class Bicycle:
    def run(self, km):
        print(f'一共用脚骑了{km}，累死了')

# 电动车类
# 继承：把父类的名称放在类名的小括号里
class EBicycle(Bicycle):
    # 属性需要传参定义，可以直接放在构造函数中
    def __init__(self, valume):
        self.valume = valume

    # 充电方法
    def fill_charge(self, vol):
        # 充电后电量 = 本身的电量 + 充电的电量
        self.valume += vol
        print(f'充了{vol}度电，现在的电量为{self.valume}度')

    # 骑行方法，重写父类的run方法
    def run(self, km):
        # 1. 获取目前电量所能电动骑行的最大里程数
        power_km = self.valume * 10

        if power_km >= km:
            print(f'我使用电动车骑行了{km}公里')
        else:
            # 电量不够了，电量用完后需要用脚骑
            print(f'我使用电动车骑行了{power_km}公里')
            # 电量耗尽时调用Bicycle中的run方法
            # 非继承调用
            # bick = Bicycle()
            # bick.run(km - power_km)
            # 继承调用，使用super()即可调用父类的属性和方法
            super().run(km-power_km)


ebick = EBicycle(2)
ebick.run(120)
# ebick.fill_charge(20)
# bick = Bicycle()
# bick.run(20)

