#!/user/bin/env python
# -*- coding: utf-8 -*-
import json

import requests as requests


def test_tag_get():
    url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
    r = requests.post(
        url,
        params={"access_token":"ACCESS_TOKEN"},
        json={
            "group_id": "GROUP_ID",
            "group_name": "GROUP_NAME",
            "order": 1,
            "tag": [{
                "name": "TAG_NAME_1",
                "order": 1
            },
            {
                "name": "TAG_NAME_2",
                "order": 2
            }
            ],
            "agentid" : 1000014
            }
    )
    print(r.json())
    print(json.dumps(r.json(), intent=2)) # intent=2 会让结果间隔两个空格
    assert r.status_code == 200
    assert r.json()['errcode'] == 0