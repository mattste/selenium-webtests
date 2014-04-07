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

        if self.browser_capabilities["browserName"] == "internet explorer":
            self._finetuneIE()          

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

        js_error = False
        console_data = []
        try:
            console_data = self.driver.execute_script("return console.getData()")
        except:
            pass

        if console_data:
            for item in console_data:
                if item["type"] == "error":
                    js_error = item
                    break

        self.driver.quit()
        swt.active_driver = None

        # fail test if there is any JS error the console
        if js_error:
            self.fail("Following JS error has occured on the page: " + json.dumps(js_error))

    def _finetuneIE(self):
        # start IE in private mode to prevent storing cookies
        self.browser_capabilities["ie.forceCreateProcessApi"] = 1
        self.browser_capabilities["ie.browserCommandLineSwitches"] = "-private"

        # seems not reliable. More testing needed.
        #self.browser_capabilities["ie.usePerProcessProxy"] = True

        # Too slow. Private mode is probably better solution for cache and cookie cleaning
        #self.browser_capabilities["ie.ensureCleanSession"] = True

        # IE seems more stable with this option
        self.browser_capabilities["ie.setProxyByServer"] = True

        # IE8 hack to prevent "...click on the element was not scrolled into the viewport" error
        if self.browser_capabilities["version"] == "8.0":
            self.browser_capabilities["elementScrollBehavior"] = 1

