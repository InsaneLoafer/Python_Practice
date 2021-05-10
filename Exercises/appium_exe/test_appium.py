#!/user/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
caps = {}
caps ["platformName"] = "Android"
caps ["deviceName"] = "insane"
caps ["appPackage"] = "com.tencent.wework"
caps ["appActivity"] = ".launch.LaunchSplashActivity"
caps ["noReset"] = "True"

driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
