#!/user/bin/env python
# -*- coding: utf-8 -*-
import json

import requests

corpid = "" # 企业id
corpsecret = ""

class Tag:

    def __init__(self):
        self.token = ""

    def get_token(self):
        """获取token"""
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={"corpid": corpid, "corpsecret": corpsecret}
        )
        self.token = r.json()["access_token"]

    def list(self):
        """获取tag列表"""
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token=": self.token},
            json={
                "tag_id":[]
            }
        )
        print(json.dumps(r.json(), intent=2))  # intent=2 会让结果间隔两个空格
        return r

    def add(self, group_name, tags):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        r = requests.post(
            url,
            params={"access_token": self.token},
            json={
                "group_id": "GROUP_ID",
                "group_name": group_name,
                "order": 1,
                "tag": tags,
                "agentid": 1000014
            }
        )
        # print(r.json())
        print(json.dumps(r.json(), intent=2))  # intent=2 会让结果间隔两个空格
        return r

