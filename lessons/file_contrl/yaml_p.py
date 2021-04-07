#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/31 21:21
# @Author   : ZhangTao
# @File     : yaml_p.py
import yaml

# 将yaml转换成Python数据
# print(yaml.load(open('demo.yml'), Loader=yaml.FullLoader)) # Loader=yaml.FullLoader可以将结果中关于yaml的描述去掉

# 将Python数据转换为yaml
data = [{'a':[1,2,3]}, 'ALLOW', 'sdf', 66]
print(yaml.dump(data))

# 将dump结果存储到文件中
with open('demo2.yml', 'w') as f:
    yaml.dump(data=data, stream=f)