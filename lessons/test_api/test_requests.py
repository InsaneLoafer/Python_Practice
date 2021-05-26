#!/user/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth

def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
        "Cookie": "Insane_Cookie",
        "User-Agent": "Insane"
    }
    r = requests.get(url, headers = header, verify=False)
    print(r.request.headers)
    print(type(r.text))
    assert "Insane" in r.text

def test_demo1():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
        "User-Agent": "Insane"
    }
    cookie_data = {
        "Insane": "Loafer",
        "Tiger": "Number1"
    }
    r = requests.get(url, headers = header, cookies = cookie_data, verify=False)
    print(r.request.headers)

def test_auth():
    r = requests.get(
        url="https://httpbin.testing-studio.com/basic-auth/insane/123",
        auth = HTTPBasicAuth("Insane", "123"),
        verify = False
        )
    print(r.request.headers)