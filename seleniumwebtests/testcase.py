# -*- coding: utf-8 -*-

import unittest

from seleniumwebtests import config
from seleniumwebtests.browser import Browser
from seleniumwebtests import myglobals

class TestCase(unittest.TestCase):
	"""
	Base class for all test cases
	"""

	def __init__(self, *args, **kwargs):
		self.proxy = myglobals.proxy
		self.browser_capabilities = myglobals.desired_browser
		super(TestCase, self).__init__(*args, **kwargs)

	def getBrowserCapabilitiesAsString(self):
		"""
		Returns browser info as string
		"""
		return self.browser_capabilities["browserName"] + "," + self.browser_capabilities["version"] + "," + self.browser_capabilities["platform"]

	def setUp(self):
		self.browser = Browser(
			"http://{0}:{1}/wd/hub".format(config.IP, config.SELENIUM_SERVER_PORT),
			self.browser_capabilities,
			proxy=self.proxy.selenium_proxy()
		)
		self.browser.set_base_url("http://zbozi.cz");
		self.browser.implicitly_wait(10)

