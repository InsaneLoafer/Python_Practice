#!/user/bin/env python
# -*- coding: utf-8 -*-
import requests


class TestDemo:
    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "insane"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_post_xml(self):
        xml = """<?xml version='1.0' encoding='utf-8'?><a>6</a>"""
        headers = {'Content-Type': 'application/xml'}
        r = requests.post('http://httpbin.org/post', data=xml, headers=headers).text


