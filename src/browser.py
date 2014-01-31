# -*- coding: utf-8 -*-

from selenium import webdriver
from conf import settings

class Browser(webdriver.Remote):

	def get(self, url):
		if not url.startswith("http"):
			url = settings.BASE_URL + url
		super(Browser, self).get(url)

