#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/26 20:44
# @Author   : InsaneLoafer
# @File     : tes_rsa.py
import requests
import base64
import json


class ApiRequest:
    # 定义请求信息
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }
    def send(self, data:dict):
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.content))

        # 把加密后的响应值发给第三方服务，让第三方服务做解密然后返回
        elif data["encoding"] == "private":
            return requests.post("url", data=res.content)

if __name__ == '__main__':
    api = ApiRequest()
    print(api.send(api.req_data))