# -*- coding: utf-8 -*-

import os
import re
import inspect
import unittest

from seleniumwebtests import config
from seleniumwebtests import testcase
from seleniumwebtests import myglobals

VALID_FILE_NAME = re.compile(r'[_a-z]\w*\.py$', re.IGNORECASE)

class TestLoader():

    def __init__(self):
        self._loader = unittest.TestLoader()

    def getTestSuite(self):
        test_suite = unittest.TestSuite()
        test_cases = self._getTestCases()

        for tc in test_cases:
            browsers = self._getBrowsers(tc)
            for b in browsers:
                myglobals.desired_browser = b
                tests = self._loader.loadTestsFromTestCase(tc)
                test_suite.addTests(tests)

        return test_suite

    def _getTestCases(self):
        test_cases = []
        files = os.listdir(os.getcwd())
        for f in files:
            if VALID_FILE_NAME.match(f):
                file_name = os.path.splitext(f)[0]
                module = __import__(file_name, globals(), locals(), ['*'])
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj):
                        if self._isTestCaseClass(obj):
                            test_cases.append(obj)
        return test_cases

    def _isTestCaseClass(self, obj):
        for parent in obj.__bases__:
            if parent.__module__ + "." + parent.__name__ == "seleniumwebtests.testcase.TestCase":
                return True
        return False

    def _getBrowsers(self, test_case):
        if hasattr(test_case, "BROWSERS"):
            return test_case.BROWSERS
        return myglobals.settings.BROWSERS
