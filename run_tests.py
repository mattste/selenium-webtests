#!/usr/bin/python
# -*- coding: utf-8 -*-

def run_tests():
	import unittest, ConfigParser, browsermobproxy, my_globals

	config = ConfigParser.RawConfigParser()
	config.read('conf/config.conf')

	#my_globals.proxy_server = browsermobproxy.Server(config.get("proxy", "startScript"), {"port": config.get("proxy", "port")})
	#my_globals.proxy_server.start()
	#my_globals.proxy = browsermobproxy.Client("{0}:{1}".format(config.get("proxy", "address"), config.get("proxy", "port")))

	test_loader = unittest.defaultTestLoader
	test_runner = unittest.TextTestRunner(verbosity=2)
	test_suite = unittest.TestSuite()

	for item in config.get("browsers", "list").split(","):
		browser = dict(config.items(item))
		my_globals.browser = browser
		test_suite.addTest(test_loader.discover(config.get("control", "suitesDir")))

	test_runner.run(test_suite)

	my_globals.proxy_server.stop()

if __name__ == "__main__":
	run_tests()
