# -*- coding: utf-8 -*-

from testcase import TestCase

class ExampleTest2(TestCase):

	def test_title(self):
		self.browser.get("http://www.zbozi.cz")
		assert u"Zboží.cz" in self.browser.title
