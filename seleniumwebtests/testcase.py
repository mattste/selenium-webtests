# -*- coding: utf-8 -*-

import unittest
import seleniumwebtests as swt

class TestCase(unittest.TestCase):
    """
    Base class for all test cases
    """

    def __init__(self, *args, **kwargs):
        self.proxy = swt.myglobals.proxy.startClient()
        self.browser_capabilities = swt.myglobals.desired_browser
        super(TestCase, self).__init__(*args, **kwargs)

    def getBrowserCapabilitiesAsString(self):
        """
        Returns browser info as string
        """
        return self.browser_capabilities["browserName"] + "," + self.browser_capabilities["version"] + "," + self.browser_capabilities["platform"]

    def setUp(self):
        self.browser = swt.Browser(
            "http://{0}:{1}/wd/hub".format(swt.config.IP, swt.config.SELENIUM_SERVER_PORT),
            self.browser_capabilities
        )

        # waits 10 sec if the DOM isn't ready immediately after page load (IE8)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.proxy.close()

