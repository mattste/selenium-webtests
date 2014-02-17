# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from runner import runner

class WebDriver(webdriver.Remote):
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
        super(WebDriver, self).get(url)

    def wait(self, timeout):
        time.sleep(timeout)
