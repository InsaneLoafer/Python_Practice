#!/user/bin/env python
# -*- coding: utf-8 -*-
from lessons.appium_test.test2.page.base_page import BasePage
from lessons.appium_test.test2.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)