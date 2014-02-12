#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import inspect
import re
import socket
import unittest
import browsermobproxy

from seleniumwebtests import reporter
from seleniumwebtests import config
from seleniumwebtests import testcase

proxy_server = None
test_runner = unittest.TextTestRunner(verbosity=2, resultclass=reporter.Reporter)
test_suite = unittest.TestSuite()
VALID_TESTCASE_FILENAME = re.compile(r'[_a-z]\w*\.py$', re.IGNORECASE)

def is_selenium_grid_hub_running():
	"""
	Method to test whether Selenium Grid HUB is running 
	on localhost port specified in the config file
	"""
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
	"""
	Starts the browsermob-proxy server and client
	The client is passed to the testcase so we can use it in our tests
	"""
	global proxy_server
	proxy_server = browsermobproxy.Server(config.PROXY_START_SCRIPT, {"port": int(config.PROXY_PORT)})
	proxy_server.start()
	testcase.proxy = browsermobproxy.Client("{0}:{1}".format(config.IP, config.PROXY_PORT))


def create_test_suite():
	"""
	Method to assembly the test suite
	"""
	global desired_browser, test_suite
	test_modules = []
	loader = unittest.TestLoader()

	# get all files from current directory
	files = os.listdir(os.getcwd())

	for f in files:
		# ignore .pyc and .pyo
		if VALID_TESTCASE_FILENAME.match(f):
			module_name = os.path.splitext(f)[0]
			# import all from the file
			module = __import__(module_name, globals(), locals(), ['*'])
			for name, obj in inspect.getmembers(module):
				# select only classes that inherit from "seleniumwebtests.testcase.TestCase"
				if inspect.isclass(obj):
					for parent in obj.__bases__:
						if parent.__module__ + "." + parent.__name__ == "seleniumwebtests.testcase.TestCase":
							test_modules.append(obj)

	# create tests for all browser defined in the testcase
	for m in test_modules:
		for b in m.BROWSERS:
			# temporary save the browser parameters so we can instantiate the testcase with them
			testcase.desired_browser = b
			tests = loader.loadTestsFromTestCase(m)
			test_suite.addTests(tests)


def main():
	# include current directory into sys.path 
	# in order to be able to import files from there
	sys.path.append(os.getcwd())
	is_selenium_grid_hub_running()
	start_proxy()
	create_test_suite()
	test_runner.run(test_suite)
	proxy_server.stop()


if __name__ == "__main__":
	main()
