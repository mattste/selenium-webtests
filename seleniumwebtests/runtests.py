#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import socket
import inspect
import re
import unittest
import browsermobproxy
from seleniumwebtests import testcase, testresult, config

proxy_server = None
test_runner = unittest.TextTestRunner(verbosity=2, resultclass=testresult.TestResult)
test_suite = unittest.TestSuite()
VALID_MODULE_NAME = re.compile(r'[_a-z]\w*\.py$', re.IGNORECASE)

def is_selenium_grid_hub_running():
	try:
		socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket_.settimeout(1)
		socket_.connect(("localhost", int(config.SELENIUM_SERVER_PORT)))
		socket_.close()
		return True
	except socket.error:
		print "Selenium Grid Hub does not running. Try execute \"java -jar {0} -role hub\".".format(config.SELENIUM_FILE)
		sys.exit()


def start_proxy():
	global proxy_server
	proxy_server = browsermobproxy.Server(config.PROXY_START_SCRIPT, {"port": int(config.PROXY_PORT)})
	proxy_server.start()
	testcase.proxy = browsermobproxy.Client("{0}:{1}".format(config.IP, config.PROXY_PORT))


def create_test_suite():
	global desired_browser, test_suite
	test_modules = []
	loader = unittest.TestLoader()
	files = os.listdir(config.TESTS_DIR)
	for f in files:
		module_name = config.TESTS_DIR + "." + os.path.splitext(f)[0]
		module = __import__(module_name, globals(), locals(), ['*'])
		for name, obj in inspect.getmembers(module):
			if inspect.isclass(obj):
				if not VALID_MODULE_NAME.match(f):
					continue
				for parent in obj.__bases__:
					if parent.__module__ + "." + parent.__name__ == "testcase.TestCase":
						test_modules.append(obj)

	for m in test_modules:
		browsers = m.browsers
		for b in browsers:
			testcase.desired_browser = b
			tests = loader.loadTestsFromTestCase(m)
			test_suite.addTests(tests)


def main():
	is_selenium_grid_hub_running()
	start_proxy()
	create_test_suite()
	test_runner.run(test_suite)
	proxy_server.stop()

if __name__ == "__main__":
	main()
