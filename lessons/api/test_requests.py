#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/24 21:12
# @Author   : InsaneLoafer
# @File     : test_requests.py
import json
import requests
from jsonpath import jsonpath
from .requests_xml import XMLSession
from hamcrest import *
from jsonschema import validate


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

    def test_post_json(self):
        payload = {
            "username": "Insane",
            "password": "loafer"
        }
        r = requests.post("http://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['usernmae'] == "Insane"

    def test_header(self):
        r = requests.get("http://httpbin.testing-studio.com/get", headers={'h': 'H'})
        print(r.text)
        assert r.status_code == 200
        assert r.json()['headers']['h'] == "H"

    def test_hogwards(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹'
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹' # 取出所有name的第一个

    def test_xml(self):
        session =  XMLSession()
        r = session.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
        r.xml.links
        item = r.xml.xpath('//item', first=True)
        print(item.text)

    def test_xml_ex(self):
        import xml.etree.ElementTree as ET
        countrydata = requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss").text
        root = ET.fromstring(countrydata)
        root.findall(".")
        root.findall("./country/neighbor")
        root.findall(".//year/..[@name='Singapore']")
        root.findall(".//*[@name='Singapore']/year")
        root.findall(".//neighbor[2]")

    def test_hamcrest(self):
        r = requests.get("http://httpbin.testing-studio.com/get", headers={'h': 'H'})
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['headers']['h'], equal_to('H'))

    def test_schema(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.load(open("topic_schema.json"))
        validate(data, schema=schema)