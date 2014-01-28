# -*- coding: utf-8 -*-

from unittest import TestCase
from selenium import webdriver
from conf.settings import my_globals
from selenium.webdriver.common.keys import Keys

class SuiteBase(TestCase):

	def __init__(self, *args, **kwargs):
		self.browser_capabilities = my_globals["browser_info"]
		super(SuiteBase, self).__init__(*args, **kwargs)

	def setUp(self):
		self.proxy = my_globals["proxy"]
		self.browser = webdriver.Remote("http://localhost:4444/wd/hub", self.browser_capabilities, proxy=self.proxy.selenium_proxy())

	def tearDown(self):
		self.browser.close()
