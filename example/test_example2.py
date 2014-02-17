# -*- coding: utf-8 -*-

from seleniumwebtests.testcase import *

class TestExample2(TestCase):

    def test_proklik(self):
        self.driver.get("/")
        assert True
