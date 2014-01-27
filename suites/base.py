# -*- coding: utf-8 -*-

import unittest, json, my_globals
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.keys import Keys

class Base(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		self.browser_capabilities = my_globals.browser
		super(Base, self).__init__(*args, **kwargs)

	def setUp(self):
		self.browser = webdriver.Remote("http://localhost:4444/wd/hub", self.browser_capabilities)

	def tearDown(self):
		self.browser.close()


