# -*- coding: utf-8 -*-

from seleniumwebtests import testcase

class TestExample2(testcase.TestCase):

	BASE_URL = "http://zbozi.cz"
	BROWSERS = [
		{
			"browserName": "firefox",
			"version": "ANY",
			"platform": "ANY"
		},
		{
			"browserName": "internet explorer",
			"version": "8.0",
			"platform": "ANY"
		}
	]

	def test_title(self):
		self.browser.get("http://zbozi.cz")
		assert u"Zboží.cz" in self.browser.title

	def tearDown(self):
		self.browser.close()
