#!/usr/bin/python
# -*- coding: utf-8 -*-

def run_tests():
	import unittest, browsermobproxy, json, my_globals

	conf = json.load(open("config.json"))

	my_globals.proxy_server = browsermobproxy.Server("/home/jk/Desktop/selenium/browsermobproxy/bin/browsermob-proxy", {"port": conf.get("proxyServerPort")})
	my_globals.proxy_server.start()
	my_globals.proxy = browsermobproxy.Client("{0}:{1}".format(conf.get("proxyServerUrl"), conf.get("proxyServerPort")))

	test_loader = unittest.defaultTestLoader
	test_runner = unittest.TextTestRunner(verbosity=2)
	test_suite = unittest.TestSuite()

	for browser in conf.get("browsers"):
		my_globals.browser = browser
		test_suite.addTest(test_loader.discover(conf.get("suitesDir")))

	test_runner.run(test_suite)

	my_globals.proxy_server.stop()

if __name__ == "__main__":
	run_tests()
