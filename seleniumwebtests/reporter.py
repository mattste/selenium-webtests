# -*- coding: utf-8 -*-

import unittest

class Reporter(unittest.runner.TextTestResult):

	def startTest(self, test):
		super(unittest.runner.TextTestResult, self).startTest(test)
		if self.showAll:
			self.stream.write(self.getDescription(test))
			self.stream.write(" on ")
			self.stream.write(test.getBrowserCapabilitiesAsString())
			self.stream.write(" ... ")
			self.stream.flush()

