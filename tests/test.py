# -*- coding: utf-8 -*-

from src.suitebase import SuiteBase

class BasicSuite(SuiteBase):

	def test_title(self):
		self.browser.get("/")
		assert u"Zboží.cz" in self.browser.title
