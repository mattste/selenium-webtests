# -*- coding: utf-8 -*-

import json
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver import WebDriver
from runner import runner

__all__ = ["json", "Keys", "WebDriverWait", "TestCase"]

class TestCase(unittest.TestCase):
    """
    Base class for all test cases
    """

    def __init__(self, *args, **kwargs):
        self.proxy = runner.proxy
        self.browser_capabilities = runner.desired_browser
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
            "http://{0}:{1}/wd/hub".format(runner.config.IP, runner.config.SELENIUM_SERVER_PORT),
            self.browser_capabilities,
            proxy=self.proxy.selenium_proxy()
        )

        self.driver.implicitly_wait(10)
        runner.active_driver = self.driver

    def tearDown(self):
        """
        Code to be executed after each test
        """
        js_errors = self.driver.execute_script('return window.jsErrors')

        self.driver.quit()
        runner.active_driver = None
        
        # fail test if there is any JS error
        if js_error:
            self.fail("There is some JS error on the page!")

