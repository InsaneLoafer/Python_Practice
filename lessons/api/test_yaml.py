#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/26 22:10
# @Author   : InsaneLoafer
# @File     : test_yaml.py
import yaml

def test_yaml():
    env = {
        "default":"dev",
        "env_select":
            {
                "dev": "127.0.0.1",
                "test": "127.0.0.2"
            }

    }
    with open("env.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)