# -*- coding: utf-8 -*-

import unittest

from runner import runner

class Reporter(unittest.runner.TextTestResult):

    def __init__(self, *args, **kwargs):
        runner.reporter_instance = self
        super(Reporter, self).__init__(*args, **kwargs)

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

