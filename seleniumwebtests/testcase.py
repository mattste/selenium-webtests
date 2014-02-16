# -*- coding: utf-8 -*-

import unittest
from browser import Browser
from runner import runner
from selenium.webdriver.common.keys import Keys

__all__ = ["Keys", "TestCase"]

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
        self.browser = Browser(
            "http://{0}:{1}/wd/hub".format(runner.config.IP, runner.config.SELENIUM_SERVER_PORT),
            self.browser_capabilities,
            proxy=self.proxy.selenium_proxy()
        )

        self.browser.implicitly_wait(10)
