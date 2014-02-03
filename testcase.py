# -*- coding: utf-8 -*-

import unittest
import settings
import run_tests
from browser import Browser
from selenium.webdriver.common.keys import Keys

class TestCase(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		self.browser_capabilities = run_tests.desired_browser
		super(TestCase, self).__init__(*args, **kwargs)

	def setUp(self):
		self.proxy = run_tests.proxy
		self.browser = Browser(
			"http://{0}:{1}/wd/hub".format(settings.IP, settings.SELENIUM_SERVER_PORT),
			self.browser_capabilities,
			proxy=self.proxy.selenium_proxy()
		)

	def tearDown(self):
		self.browser.close()
