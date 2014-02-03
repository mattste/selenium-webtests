# -*- coding: utf-8 -*-

import settings

from selenium import webdriver

class Browser(webdriver.Remote):

	def get(self, url):
		if not url.startswith("http"):
			url = settings.BASE_URL + url
		super(Browser, self).get(url)

