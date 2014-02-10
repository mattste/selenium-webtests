import config

from selenium import webdriver

class Browser(webdriver.Remote):

	def get(self, url):
		"""
		Overrides default webdriver.Remote.get method.
		If the URL passed as argument does not begins with "http"
		it is considered as relative and will be prefixed with
		config.BASE_URL string

		:param url: Destination URL
		"""
		if not url.startswith("http"):
			url = config.BASE_URL + url
		super(Browser, self).get(url)

