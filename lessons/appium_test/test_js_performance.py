#!/user/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver


class TestData:
    def test_data(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        print(driver.execute_script("return JSON.stringify(window.performance.timing)"))
        print(driver.execute_script(
            "return JSON.stringify(window.performance.getEntriesByName(document.querySelector('img').src)[0], null, 2)"))