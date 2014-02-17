# -*- coding: utf-8 -*-

from seleniumwebtests.testcase import *

class TestExample(TestCase):

    def test_proklik(self):
        self.driver.get("/")
        self.proxy.new_har("test")
        self.driver.find_element_by_css_selector(".box-content").click()
        self.assertTrue(self.proxy.find_in_har(
            "hellfire.dev", {
                "response.statusText": "OK",
                "response.status": 200,
                "response.headers": {
                    "name": "Connection",
                    "value": "close"
                }
            }
        ))
