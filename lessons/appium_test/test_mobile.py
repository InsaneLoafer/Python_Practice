#!/usr/bin/python3
# -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestParam:
    def setup(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.main.view.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = "true"
        """当要输入中文时需要以下两个参数"""
        desired_caps['unicodeKeyBoard']='true'
        desired_caps['resetKeyBoard']='true'
        desired_caps['newCommandTimeout'] = 400
        # # 超时时间
        # desired_caps['adbExecTimeout'] = 500000
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        # 模拟打电话
        self.driver.make_gsm_call('13612312312', GsmCallActions.CALL)
        # 模拟发短信
        self.driver.send_sms('13612312312', 'hello appium apis')
        # 模拟网络设置，设置为飞行模式
        self.driver.set_network_connection(1)
        sleep(3)
        # 模拟网络设置，设置为数据模式
        self.driver.set_network_connection(4)
        # 获取截图并保存到路径中
        self.driver.get_screenshot_as_file('./photos/img.png')
        """
        进行录屏操作
        1.开始录屏
        2.停止录屏
        3.只支持Android8.0以上版本，且部分手机如华为不支持
        """
        self.driver.start_recording_screen()
        self.driver.stop_recording_screen()
