# -*- coding: utf-8 -*-

from suitebase import SuiteBase

class BasicSuite2(SuiteBase):

	def test_title(self):
		self.browser.get("http://www.zbozi.cz")
		assert u"Zboží.cz" in self.browser.title
