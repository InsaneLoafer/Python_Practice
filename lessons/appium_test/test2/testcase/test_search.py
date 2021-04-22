#!/user/bin/env python
# -*- coding: utf-8 -*-
from lessons.appium_test.test2.page.app import App


class TestSearch:

    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")