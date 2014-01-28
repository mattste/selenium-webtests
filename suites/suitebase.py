# -*- coding: utf-8 -*-

from conf import settings
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SuiteBase(TestCase):

	def __init__(self, *args, **kwargs):
		self.browser_capabilities = settings.tmp_browser_info
		super(SuiteBase, self).__init__(*args, **kwargs)

	def setUp(self):
		self.proxy = settings.proxy
		self.browser = webdriver.Remote("http://localhost:4444/wd/hub", self.browser_capabilities, proxy=self.proxy.selenium_proxy())

	def tearDown(self):
		self.browser.close()
