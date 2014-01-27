# -*- coding: utf-8 -*-

import unittest
from browserprovider import bbrowser
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.keys import Keys

class Base(unittest.TestCase):

	def setUp(self):
		global bbrowser
		self.browser = webdriver.Remote("http://localhost:4444/wd/hub", bbrowser)

	def tearDown(self):
		self.browser.close()


