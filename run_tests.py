#!/usr/bin/python
# -*- coding: utf-8 -*-

def run_tests():
	import unittest, json, my_globals

	conf = json.load(open("config.json"))
	test_loader = unittest.defaultTestLoader
	test_runner = unittest.TextTestRunner(verbosity=2)
	test_suite = unittest.TestSuite()

	for browser in conf.get("browsers"):
		my_globals.browser = browser
		test_suite.addTest(test_loader.discover(conf.get("suitesDir")))

	test_runner.run(test_suite)

if __name__ == "__main__":
	run_tests()
