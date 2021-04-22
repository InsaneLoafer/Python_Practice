#!/user/bin/env python
# -*- coding: utf-8 -*-
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    _black_list = [(By.ID, "image_cancel")] # 定义弹窗黑名单
    _error_count = 0 # 设置弹窗遍历的计数器
    _error_max = 10  # 设置最大的遍历次数
    _params = {} # 设置send_keys的值字典
    def __init__(self, driver:WebDriver=None):
        self._driver = driver

    def find(self, by, locator=None):

        """
        使用三目表达式，如果使用find((By.ID, "name")) 的tuple形式也能识别
        并且进行弹窗处理
        """
        try:
            # 如果找到了元素，就将计数器置零，并返回元素
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_count = 0
            return element
        except Exception as e:
            # 如果有弹窗，就将计数器加1直到大于最大的遍历数，抛出异常
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            # 遍历弹窗黑名单
            for black in self._black_list:
                # 搜索黑名单元素，并返回列表
                elements = self._driver.find_elements(*black)
                # 如果元素列表不为0，则点击元素即点击弹框
                if len(elements) > 0:
                    elements[0].click()
                    # 然后递归find方法，循环遍历
                    return self.find(by, locator)
            raise e

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            # 如果有弹窗，就将计数器加1直到大于最大的遍历数，抛出异常
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            # 遍历弹窗黑名单
            for black in self._black_list:
                # 搜索黑名单元素，并返回列表
                elements = self._driver.find_elements(*black)
                # 如果元素列表不为0，则点击元素即点击弹框
                if len(elements) > 0:
                    elements[0].click()
                    # 然后递归find方法，循环遍历
                    return self.send(value, by, locator)
            raise e


    def steps(self, path):
        """
        读取yaml文件
        :param path: yaml文件路径
        :return:
        """
        with open(path, encoding='utf-8') as f:
            # steps为list
            steps :list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if 'click' == step["action"]:
                        element.click()
                    if 'send' == step["action"]:
                        # 替换yaml文件中的{value}值
                        content:str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}"%param, self._params[param])
                        self.send(content, step["by"], step["locator"])



