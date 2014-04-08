# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime
import unittest
import xmlrunner

from seleniumwebtests import swt

class _TestResult(xmlrunner._XMLTestResult):

    def __init__(self, *args, **kwargs):
        swt.reporter_instance = self
        super(_TestResult, self).__init__(*args, **kwargs)

    def startTest(self, test):
        """
        Called before execute each test method.
        """
        self.start_time = time.time()
        unittest.TestResult.startTest(self, test)

        if self.showAll:
            self.stream.write(self.getDescription(test))
            self.stream.write(" on ")
            self.stream.write(test.stringify_browser_capabilities())
            self.stream.write(" ... ")
            self.stream.flush()      

class TestRunner(xmlrunner.XMLTestRunner):

    def __init__(self, *args, **kwargs):
        super(TestRunner, self).__init__(*args, **kwargs)

    def _make_result(self):
        """
        Creates a TestResult object which will be used to store
        information about the executed tests.
        """
        return _TestResult(
            self.stream, self.descriptions, self.verbosity, self.elapsed_times
        )

    def run(self, test):
        """
        Runs the given test case or test suite.
        """
        try:
            # Prepare the test execution
            self._patch_standard_output()
            result = self._make_result()

            # Print a nice header
            self.stream.writeln()
            self.stream.writeln('Running tests...')
            self.stream.writeln(result.separator2)

            # Execute tests
            start_time = time.time()
            test(result)
            stop_time = time.time()
            time_taken = stop_time - start_time

            # Print results
            result.printErrors()
            self.stream.writeln(result.separator2)
            run = result.testsRun
            self.stream.writeln("Ran %d test%s in %.3fs" % (
                run, run != 1 and "s" or "", time_taken)
            )
            self.stream.writeln()

            expectedFails = unexpectedSuccesses = skipped = 0
            try:
                results = map(len, (result.expectedFailures,
                                    result.unexpectedSuccesses,
                                    result.skipped))
            except AttributeError:
                pass
            else:
                expectedFails, unexpectedSuccesses, skipped = results

            # Error traces
            infos = []
            if not result.wasSuccessful():
                self.stream.write("FAILED")
                failed, errored = map(len, (result.failures, result.errors))
                if failed:
                    infos.append("failures={0}".format(failed))
                if errored:
                    infos.append("errors={0}".format(errored))
            else:
                self.stream.write("OK")

            if skipped:
                infos.append("skipped={0}".format(skipped))
            if expectedFails:
                infos.append("expected failures={0}".format(expectedFails))
            if unexpectedSuccesses:
                infos.append("unexpected successes={0}".fornat(unexpectedSuccesses))

            if infos:
                self.stream.writeln(" ({0})".format(", ".join(infos)))
            else:
                self.stream.write("\n")

            # Generate reports
            if swt.config.XML_RESULT:
                self.stream.writeln()
                self.stream.writeln('Generating XML reports...')
                result.generate_reports(self)
        finally:
            self._restore_standard_output()

        return result
