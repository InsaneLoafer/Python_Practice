#!/user/bin/env python
# -*- coding: utf-8 -*-
from lessons.appium_test.test2.page.base_page import BasePage
from lessons.appium_test.test2.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)