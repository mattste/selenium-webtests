#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, socket, inspect, re
import unittest
import settings
import testcase
import browsermobproxy as bmp

proxy_server = None
proxy = None
desired_browser = None
test_runner = unittest.TextTestRunner(verbosity=2)
test_suite = unittest.TestSuite
VALID_MODULE_NAME = re.compile(r'[_a-z]\w*\.py$', re.IGNORECASE)

def is_selenium_grid_hub_running():
	try:
		socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket_.settimeout(1)
		socket_.connect(("localhost", settings.SELENIUM_SERVER_PORT))
		socket_.close()
		return True
	except socket.error:
		print "Selenium Grid Hub does not running. Try execute \"java -jar {0} -role hub\".".format(settings.SELENIUM_SERVER_FILE)
		sys.exit()


def start_proxy():
	global proxy_server, proxy
	proxy_server = bmp.Server(settings.PROXY_START_SCRIPT, {"port": settings.PROXY_PORT})
	proxy_server.start()
	proxy = bmp.Client("{0}:{1}".format(settings.IP, settings.PROXY_PORT))


def create_test_suite():
	global desired_browser, test_suite
	test_loader = unittest.TestLoader()
	files = os.listdir(settings.TESTS_DIR)
	for f in files:
		module_name = settings.TESTS_DIR + "." + os.path.splitext(f)[0]
		module = __import__(module_name, globals(), locals(), ['*'])
		for name, obj in inspect.getmembers(module):
			if inspect.isclass(obj):
				if not VALID_MODULE_NAME.match(f):
					continue
				#if obj.__module__ + "." + obj.__class__.__name__ == "testcase."

	'''
	loader = unittest.TestLoader()
	tests = loader.discover(settings.TESTS_DIR)
	for test in tests:
		browsers = settings.BROWSERS
		if hasattr(test, "browsers"):
			browsers = tests.browsers
		for browser in browsers:
			test_suite.addTest(test)

		print test_suite.getTests()[0].__class__.__name__
	'''

def get_tests():
	tests = []
	paths = os.listdir(settings.TESTS_DIR)

	for path in paths:
		p = os.path.splitext(os.path.normpath(path))[0]
		rp = os.path.relpath(p)
		name = rp.replace(os.path.sep, '.')

	__import__(name)
	test.append[sys.modules[name]]


def main():
	#is_selenium_grid_hub_running()
	#start_proxy()
	create_test_suite()
	#test_runner.run(test_suite)
	#proxy_server.stop()

if __name__ == "__main__":
	main()
