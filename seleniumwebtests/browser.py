# -*- coding: utf-8 -*-

from selenium import webdriver
from runner import runner

class Browser(webdriver.Remote):
	"""
	Extends selenium Remote webdriver
	"""

	def get(self, url):
		"""
		Overrides default webdriver.Remote.get method.
		If the URL passed as argument does not begins with "http"
		it is considered as relative and will be prefixed with
		testcase.BASE_URL string

		:param url: Destination URL
		"""
		if not url.startswith("http"):
			url = runner.test_settings.BASE_URL + url
		super(Browser, self).get(url)

