# -*- coding: utf-8 -*-

from unittest import TestCase
from browser import Browser
from conf import settings
from conf.settings import my_globals
from selenium.webdriver.common.keys import Keys

class SuiteBase(TestCase):

	def __init__(self, *args, **kwargs):
		self.browser_capabilities = my_globals["desired_browser"]
		super(SuiteBase, self).__init__(*args, **kwargs)

	def setUp(self):
		self.proxy = my_globals["proxy"]
		self.browser = Browser(
			"http://{0}:{1}/wd/hub".format(settings.IP, settings.SELENIUM_SERVER_PORT),
			self.browser_capabilities,
			proxy=self.proxy.selenium_proxy()
		)

	def tearDown(self):
		self.browser.close()
