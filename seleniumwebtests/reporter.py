# -*- coding: utf-8 -*-

import unittest

class Reporter(unittest.runner.TextTestResult):

    def startTest(self, test):
        """
        Adds browser info into results showing in terminal
        """
        super(unittest.runner.TextTestResult, self).startTest(test)
        if self.showAll:
            self.stream.write(self.getDescription(test))
            self.stream.write(" on ")
            self.stream.write(test.stringify_browser_capabilities())
            self.stream.write(" ... ")
            self.stream.flush()

