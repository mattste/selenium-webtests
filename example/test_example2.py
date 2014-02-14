# -*- coding: utf-8 -*-

from seleniumwebtests.testcase import *

class TestExample2(TestCase):

    def test_proklik(self):
        self.browser.get("/")
        input = self.browser.find_element_by_id("q")
        input.send_keys("notebooky")
        input.send_keys(Keys.RETURN)
        self.browser.find_element_by_css_selector(".itemlink").click()
        self.proxy.new_har("proklik")
        self.browser.find_elements_by_css_selector(".itemlink")[1].click()
        print len(self.proxy.har.get("log").get("entries"))
        assert True
