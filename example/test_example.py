# -*- coding: utf-8 -*-

from seleniumwebtests import testcase

class TestExample(testcase.TestCase):

	BASE_URL = "http://zbozi.cz"
	BROWSERS = [
		{
			"browserName": "firefox",
			"version": "ANY",
			"platform": "ANY"
		}
	]

	def test_title(self):
		self.browser.get("/")
		assert u"Zboží.cz" in self.browser.title
