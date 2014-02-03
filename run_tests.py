#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, socket
import unittest
import settings
import browsermobproxy as bmp

proxy_server = None
proxy = None
desired_browser = None
test_runner = unittest.TextTestRunner(verbosity=2)
test_suite = unittest.TestSuite()

def start_selenium_grid_hub():
	pass

def start_proxy():
	global proxy_server, proxy
	proxy_server = bmp.Server(settings.PROXY_START_SCRIPT, {"port": settings.PROXY_PORT})
	proxy_server.start()
	proxy = bmp.Client("{0}:{1}".format(settings.IP, settings.PROXY_PORT))

def create_test_suite():
	global desired_browser, test_suite
	loader = unittest.defaultTestLoader
	for item in settings.BROWSERS:
		desired_browser = item
		test_suite.addTest(loader.discover(settings.TESTS_DIR))

def is_selenium_grid_hub_running():
	try:
		socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket_.settimeout(1)
		socket_.connect(("localhost", settings.SELENIUM_SERVER_PORT))
		socket_.close()
		return True
	except socket.error:
		return False

def main():

	if not is_selenium_grid_hub_running():
		start_selenium_grid_hub()

	start_proxy()

	create_test_suite()

	test_runner.run(test_suite)

	proxy_server.stop()

if __name__ == "__main__":
	main()

