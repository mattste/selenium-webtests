# -*- coding: utf-8 -*-

import os
import sys
import time
import unittest
import xmlrunner

from seleniumwebtests import swt

def getTestRunner():
    if swt.config.XML_RESULT == True:
        return XMLTestRunner(verbosity=2, output=swt.config.XML_FILE_PATH)
    return unittest.TextTestRunner(verbosity=2, resultclass=_TextTestResult)

def printTestInfo(self, test):
    self.stream.write(self.getDescription(test))
    self.stream.write(" on ")
    self.stream.write(test.stringify_browser_capabilities())
    self.stream.write(" ... ")
    self.stream.flush()

class _TextTestResult(unittest.runner.TextTestResult):

    def __init__(self, *args, **kwargs):
        swt.reporter_instance = self
        super(_TextTestResult, self).__init__(*args, **kwargs)

    def startTest(self, test):
        """
        Adds browser info into results showing in terminal
        """
        super(unittest.runner.TextTestResult, self).startTest(test)

        if self.showAll:
            printTestInfo(self, test)

class _XMLTestResult(xmlrunner._XMLTestResult):

    def __init__(self, *args, **kwargs):
        swt.reporter_instance = self
        super(_XMLTestResult, self).__init__(*args, **kwargs)

    def startTest(self, test):
        """
        Called before execute each test method.
        """
        self.start_time = time.time()
        unittest.TestResult.startTest(self, test)

        if self.showAll:
            printTestInfo(self, test)

class XMLTestRunner(xmlrunner.XMLTestRunner):

    def __init__(self, *args, **kwargs):
        super(XMLTestRunner, self).__init__(*args, **kwargs)

    def _make_result(self):
        """
        Creates a TestResult object which will be used to store
        information about the executed tests.
        """
        return _XMLTestResult(
            self.stream, self.descriptions, self.verbosity, self.elapsed_times
        )
