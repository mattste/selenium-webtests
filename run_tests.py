#!/usr/bin/python
# -*- coding: utf-8 -*-

def run_tests():
	import json
	import unittest
	from browserprovider import bbrowser

	conf = json.load(open("config.json"))
	test_loader = unittest.defaultTestLoader
	test_runner = unittest.TextTestRunner(verbosity=2)
	test_suite = unittest.TestSuite()
	test_suite.addTest(test_loader.discover(conf.get("suitesDir")))

	for browser in conf.get("browsers"):
		bbrowser = browser
		test_runner.run(test_suite)

if __name__ == "__main__":
	run_tests()
