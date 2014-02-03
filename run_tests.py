#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, socket
import unittest
import settings
import browsermobproxy as bmp

proxy_server = None
proxy = None
desired_browser = None
test_runner = unittest.TextTestRunner(verbosity=2)
test_suite = unittest.TestSuite()

def is_selenium_grid_hub_running():
	try:
		socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket_.settimeout(1)
		socket_.connect(("localhost", settings.SELENIUM_SERVER_PORT))
		socket_.close()
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
	tests = get_tests()
	print tests
	for test in tests:
		browsers = settings.BROWSERS
		if test.browsers:
			browsers = tests.browsers
		for browser in browsers:
			desired_browser = browser
			test_suite.addTest(test)

	'''
	global desired_browser, test_suite
	loader = unittest.defaultTestLoader
	for item in settings.BROWSERS:
		desired_browser = item
		test_suite.addTest(loader.discover(settings.TESTS_DIR))
	'''

def get_tests():
	tests = []
	paths = os.listdir(settings.TESTS_DIR)

	for path in paths:
		p = os.path.splitext(os.path.normpath(path))[0]
		rp = os.path.relpath(p)
		print rp
		name = rp.replace(os.path.sep, '.')

	__import__(name)
	test.append[sys.modules[name]]

def main():
	is_selenium_grid_hub_running()
	start_proxy()
	create_test_suite()
	test_runner.run(test_suite)
	proxy_server.stop()

if __name__ == "__main__":
	main()

