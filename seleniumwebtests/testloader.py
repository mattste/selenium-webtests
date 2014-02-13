# -*- coding: utf-8 -*-

import os
import re
import inspect
import unittest
import seleniumwebtests as swt

# regexp to ignore .pyc and .pyo files
VALID_FILE_NAME = re.compile(r'[_a-z]\w*\.py$', re.IGNORECASE)

class TestLoader():

    def __init__(self):
        self._loader = unittest.TestLoader()

    def getTestSuite(self):
        """
        Returns test suite for test runner
        """
        test_suite = unittest.TestSuite()
        test_cases = self._getTestCases()

        for tc in test_cases:
            browsers = self._getBrowsers(tc)
            for b in browsers:
                swt.myglobals.desired_browser = b
                tests = self._loader.loadTestsFromTestCase(tc)
                test_suite.addTests(tests)

        return test_suite

    def _getTestCases(self):
        """
        Inspect all properties in all files in current directory
        and tests if its a test case class
        Return list of test case classes
        """
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
        """
        Tests whether the class inherits from "seleniumwebtests.testcase.TestCase"
        """
        for parent in obj.__bases__:
            if parent.__module__ + "." + parent.__name__ == "seleniumwebtests.testcase.TestCase":
                return True
        return False

    def _getBrowsers(self, test_case):
        """
        Retuns list of browsers to run the test case on
        If test case does not provide such an information
        the settigs.BROWSERS is returned
        """
        if hasattr(test_case, "BROWSERS"):
            return test_case.BROWSERS
        return swt.myglobals.settings.BROWSERS
