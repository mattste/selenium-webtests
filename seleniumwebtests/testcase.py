# -*- coding: utf-8 -*-

import sys
import os
import json
import unittest
import datetime
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
        self.logger = None
        self.proxy = swt.proxy
        self._browser_capabilities = swt.desired_browser

        if self._browser_capabilities["browserName"] == "internet explorer":
            self._finetuneIE()

        super(TestCase, self).__init__(*args, **kwargs)


    def stringifyBrowserCapabilities(self, delimiter=","):
        """
        Returns browser info as string

        :param delimiter: Character to be used as properties delimiter
        """

        return self._browser_capabilities["browserName"] + delimiter + self._browser_capabilities["version"] + delimiter + self._browser_capabilities["platform"]


    def setUp(self):
        """
        Code to be executed before each test
        """

        self.driver = WebDriver(
            "http://{0}:{1}/wd/hub".format(swt.config.ADDRESS, swt.config.SELENIUM_SERVER_PORT),
            self._browser_capabilities,
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

        self._checkJSErrors()
        self.driver.quit()
        swt.active_driver = None


    def retry(self):
        """
        Will append this test at the end of test suite.
        """
        
        swt.retried_tests.append(self.id())
        swt.desired_browser = self._browser_capabilities
        test = swt.test_loader.load_tests_from_name(self.id())
        swt.test_suite.addTests(test)
        

    def take_screenshot(self):
        """
        Takes screenshot.
        """
        try:
            filename = self.id()
            filename += "-on-" + self.stringifyBrowserCapabilities("_")
            filename += "-at-" + datetime.datetime.now().isoformat()
            filename += ".png"
            self.driver.get_screenshot_as_file(os.path.normpath(swt.config.SCREENSHOTS_DIR) + os.sep + filename)
        except:
            pass


    def _checkJSErrors(self):
        """
        Checks if "console.getData()" JS command returns some error. If so, the test will fail.
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

        # fail test if there is any JS error in the console
        if js_error:
            self.fail("An JS error has occured on the page: " + json.dumps(js_error))


    def _finetuneIE(self):
        """
        Some special settings for IE to make the browser more stable.
        """

        # start IE in private mode to prevent storing cookies
        self._browser_capabilities["ie.forceCreateProcessApi"] = 1
        self._browser_capabilities["ie.browserCommandLineSwitches"] = "-private"

        # seems not reliable. More testing needed.
        #self._browser_capabilities["ie.usePerProcessProxy"] = True

        # Too slow. Private mode is probably better solution for cache and cookie cleaning
        #self._browser_capabilities["ie.ensureCleanSession"] = True

        # IE seems to be more stable with this option
        self._browser_capabilities["ie.setProxyByServer"] = True

        # IE8 hack to prevent "...click on the element was not scrolled into the viewport" error
        if self._browser_capabilities["version"] == "8.0":
            self._browser_capabilities["elementScrollBehavior"] = 1

