# -*- coding: utf-8 -*-

import unittest
import settings
from browser import Browser
from selenium.webdriver.common.keys import Keys

proxy = None
desired_browser = None

class TestCase(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		self.proxy = proxy.selenium_proxy()
		self.browser_capabilities = desired_browser
		super(TestCase, self).__init__(*args, **kwargs)

	def setUp(self):
		self.browser = Browser(
			"http://{0}:{1}/wd/hub".format(settings.IP, settings.SELENIUM_SERVER_PORT),
			self.browser_capabilities,
			proxy=self.proxy
		)

	def tearDown(self):
		self.browser.close()
