#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/26 21:47
# @Author   : InsaneLoafer
# @File     : env_demo.py
"""
 在请求之前,对请求的url进行替换
1. 需要二次封装requests，对请求进行定制化。
2. 将请求的结构体的url从一个写死的ip地址改为一个（任意的）域名。
3. 使用一个env 配置文件，存放各个环境的配置信息。
4. 然后将请求结构体中的url替换为`env`配置文件中个人选择的url。
5. 将env配置文件使用yaml进行管理。
"""
import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yaml"))
    data = {
        "method": "get",
        "url": "http://testing-studio:9999/demo.txt",
        "headers": None,
    }

    # data是一个请求的信息
    def send(self, data:dict):
        # 进行替换
        data["url"] = str(data["url"]).replace("testing-studio", self.env["env_select"][self.env["default"]])
        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
        return r

if __name__ == '__main__':
    api = Api()
    print(api.send(api.data).text)