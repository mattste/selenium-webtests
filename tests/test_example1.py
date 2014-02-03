# -*- coding: utf-8 -*-

from testcase import TestCase

class TestExample(TestCase):

	def test_title(self):
		self.browser.get("/")
		assert u"Zboží.cz" in self.browser.title
