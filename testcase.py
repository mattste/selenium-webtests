# -*- coding: utf-8 -*-

import unittest
import settings
from run_tests import proxy, desired_browser
from browser import Browser
from selenium.webdriver.common.keys import Keys

class TestCase(unittest.TestCase):

	browsers = [
		{
			"browserName": "firefox",
			"version": "ANY",
			"platform": "ANY"
		},
		{
			"browserName": "internet explorer",
			"version": "8.0",
			"platform": "ANY"
		},
	]

	def __init__(self, *args, **kwargs):
		self.browser_capabilities = desired_browser
		super(TestCase, self).__init__(*args, **kwargs)

	def setUp(self):
		self.proxy = proxy
		self.browser = Browser(
			"http://{0}:{1}/wd/hub".format(settings.IP, settings.SELENIUM_SERVER_PORT),
			self.browser_capabilities,
			proxy=self.proxy.selenium_proxy()
		)

	def tearDown(self):
		self.browser.close()
