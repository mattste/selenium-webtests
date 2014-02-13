# -*- coding: utf-8 -*-

from seleniumwebtests import *
from selenium.webdriver.common.keys import Keys

class TestExample(testcase.TestCase):

	def test_proklik(self):
		self.browser.get("/")
		input = self.browser.find_element_by_id("q")
		input.send_keys("notebooky")
		input.send_keys(Keys.RETURN)
		self.browser.find_element_by_css_selector(".itemlink").click()
		self.proxy.new_har("proklik")
		self.browser.find_element_by_css_selector(".itemlink").click()
		print self.proxy.har



