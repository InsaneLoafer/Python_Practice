#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/24 21:12
# @Author   : InsaneLoafer
# @File     : test_requests.py
import requests


class TestDemo:
    def test_get(self):
        r = requests.get("http://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "insane"
        }
        r = requests.get("http://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "username": "Insane",
            "password": "loafer"
        }
        r = requests.post("http://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200