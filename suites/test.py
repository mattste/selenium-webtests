# -*- coding: utf-8 -*-

from suitebase import SuiteBase

class BasicSuite(SuiteBase):

	def test_title(self):
		self.browser.get("http://www.zbozi.cz")
		print self.browser.desired_capabilities
		assert u"Zboží.cz" in self.browser.title
