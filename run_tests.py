#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import browsermobproxy as bmp
from conf import settings
from conf.settings import my_globals

# globals
proxy_server = None
suite = None
test_runner = None

def run_tests():
	global proxy_server, suite, test_runner

	System.setProperty("webdriver.chrome.driver", "C:/chromedriver.exe");

	# start proxy
	proxy_server = bmp.Server(settings.PROXY_START_SCRIPT, {"port": settings.PROXY_PORT})
	proxy_server.start()
	my_globals["proxy"] = bmp.Client("{0}:{1}".format(settings.PROXY_ADDRESS, settings.PROXY_PORT))

	# create suite and run
	suite = create_suite()
	test_runner.run(suite)

	# stop proxy
	proxy_server.stop()

def create_suite():
	global test_runner

	test_runner = unittest.TextTestRunner(verbosity=2)
	suite = unittest.TestSuite()
	loader = unittest.defaultTestLoader

	for item in settings.BROWSERS:
		my_globals["browser_info"] = item
		suite.addTest(loader.discover(settings.SUITES_DIR))

	return suite

if __name__ == "__main__":
	run_tests()
