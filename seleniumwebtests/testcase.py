# -*- coding: utf-8 -*-

import json
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

from seleniumwebtests import swt
from webdriver import WebDriver

__all__ = ["json", "Keys", "WebDriverWait", "TestCase", "ActionChains", "Alert"]

class TestCase(unittest.TestCase):
    """
    Base class for all test cases
    """

    def __init__(self, *args, **kwargs):
        self.proxy = swt.proxy
        self.browser_capabilities = swt.desired_browser

        # IE8 hack to prevent "...click on the element was not scrolled into the viewport" error
        if self.browser_capabilities["version"] == "8.0":
            self.browser_capabilities["elementScrollBehavior"] = 1

        super(TestCase, self).__init__(*args, **kwargs)

    def stringify_browser_capabilities(self):
        """
        Returns browser info as string
        """
        return self.browser_capabilities["browserName"] + "," + self.browser_capabilities["version"] + "," + self.browser_capabilities["platform"]

    def setUp(self):
        """
        Code to be executed before each test
        """
        self.driver = WebDriver(
            "http://{0}:{1}/wd/hub".format(swt.config.ADDRESS, swt.config.SELENIUM_SERVER_PORT),
            self.browser_capabilities,
            proxy=self.proxy.selenium_proxy()
        )
        swt.active_driver = self.driver

    def run(self, result=None):
        try:
            super(TestCase, self).run(result)
        except:
            self.tearDown()


    def tearDown(self):
        """
        Code to be executed after each test
        """

        try:
            js_errors = self.driver.execute_script('return window.jsErrors')
        except:
            js_errors = None


        self.driver.quit()
        swt.active_driver = None

        # fail test if there is any JS error
        if js_errors:
            self.fail("There is some JS error on the page!")

