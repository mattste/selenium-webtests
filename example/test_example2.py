# -*- coding: utf-8 -*-

from seleniumwebtests import *
from selenium.webdriver.common.keys import Keys

class TestExample2(testcase.TestCase):

	def test_title(self):
		self.browser.get("http://zbozi.cz")
		assert u"Zboží.cz" in self.browser.title
