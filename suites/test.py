# -*- coding: utf-8 -*-

from base import *

class BasicSuite(Base):

	def test_title(self):
		self.browser.get("http://www.zbozi.cz")
		assert u"Zboží.cz" in self.browser.title
