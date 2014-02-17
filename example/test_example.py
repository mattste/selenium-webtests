# -*- coding: utf-8 -*-

from seleniumwebtests.testcase import *

class TestExample(TestCase):

	def test_proklik(self):
		self.driver.get("/")
		input = self.driver.find_element_by_id("q")
		input.send_keys("notebooky")
		input.send_keys(Keys.RETURN)
		self.driver.find_element_by_css_selector(".itemlink").click()
		self.proxy.new_har("proklik")
		self.driver.find_element_by_css_selector(".itemlink").click()
		print len(self.proxy.har.get("log").get("entries"))
		assert True
