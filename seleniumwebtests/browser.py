from selenium import webdriver

class Browser(webdriver.Remote):

	def set_base_url(self, url):
		self.base_url = url

	def get(self, url):
		"""
		Overrides default webdriver.Remote.get method.
		If the URL passed as argument does not begins with "http"
		it is considered as relative and will be prefixed with
		testcase.BASE_URL string

		:param url: Destination URL
		"""
		if not url.startswith("http"):
			url = self.base_url + url
		super(Browser, self).get(url)

