#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import browsermobproxy as bmp
from conf import settings
from conf.settings import my_globals

# start proxy
proxy_server = bmp.Server(settings.PROXY_START_SCRIPT, {"port": settings.PROXY_PORT})
proxy_server.start()
my_globals["proxy"] = bmp.Client("{0}:{1}".format(settings.IP, settings.PROXY_PORT))


# create suite and run
test_runner = unittest.TextTestRunner(verbosity=2)
suite = unittest.TestSuite()
loader = unittest.defaultTestLoader

for item in settings.BROWSERS:
	my_globals["desired_browser"] = item
	suite.addTest(loader.discover(settings.TESTS_DIR))

test_runner.run(suite)

# stop proxy
proxy_server.stop()
