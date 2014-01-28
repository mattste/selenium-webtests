#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import browsermobproxy as bmp
from conf import settings

class TestRunner:

	def __init__(self):

		# start proxy
		self.proxy_server = None
		settings.proxy = self.start_proxy()

		# create test suite
		self.suite = self.create_suite()

		# run tests
		self.run_tests()

		# stop the proxy
		self.stop_proxy()

	def start_proxy(self):
		self.proxy_server = bmp.Server(settings.PROXY_START_SCRIPT, {"port": settings.PROXY_PORT})
		self.proxy_server.start()
		return bmp.Client("{0}:{1}".format(settings.PROXY_ADDRESS, settings.PROXY_PORT))

	def stop_proxy(self):
		self.proxy_server.stop()

	def create_suite(self):
		self.test_runner = unittest.TextTestRunner(verbosity=2)
		suite = unittest.TestSuite()
		loader = unittest.defaultTestLoader
		for item in settings.BROWSERS:
			settings.tmp_browser_info = item
			suite.addTest(loader.discover(settings.SUITES_DIR))
		return suite

	def run_tests(self):
		self.test_runner.run(self.suite)

if __name__ == "__main__":
	TestRunner()
