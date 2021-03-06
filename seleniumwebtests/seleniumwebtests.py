# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess
import socket
import inspect
import unittest
import browsermobproxy

import config
from proxy import Proxy

class SeleniumWebtests(object):

    def __init__(self):

        self._config = config

        # load test settings
        sys.path.append(os.getcwd())
        self.set_options(vars(__import__("settings")))

        self._start_proxy_server()
        self._start_selenium_hub()

        self._proxy = None # proxy client
        self._desired_browser = None # variable for storing desired browser capabilities
        self._active_driver = None # currently running webdriver
        self._reporter_instance = None # instance of testrunner class. We need this to be able to stop test execution on CTRL+C
        self._test_loader = None
        self._test_suite = None
        self.retried_tests = []

    def run(self):
        """
        Creates test suite and runs the tests
        """
        import testrunner
        import testloader

        self._proxy = Proxy("{0}:{1}".format(self.config.ADDRESS, self.config.PROXY_SERVER_PORT))
        self._test_runner = testrunner.TestRunner(verbosity=2, output=swt.config.XML_FILE_DIR)
        self._test_loader = testloader.TestLoader()
        self._test_suite = self._test_loader.get_test_suite()
        self._test_runner.run(self._test_suite)
        self.end()

    def end(self):
        self.reporter_instance.stop()
        self._proxy.close()
        if self.active_driver:
            self.active_driver.quit()

    def set_options(self, options):
        for key in options:
            if options[key] != None:
                setattr(config, key, options[key])

    def _start_selenium_hub(self):
        if not self._is_listening(self.config.ADDRESS, self.config.SELENIUM_SERVER_PORT):
            print "Selenium HUB seems not running. Trying to start on {0}:{1}...".format(self.config.ADDRESS, self.config.SELENIUM_SERVER_PORT)
            command = ["java", "-jar", "{0}".format(self.config.SELENIUM_FILE), "-role", "hub", "-port", "{0}".format(self.config.SELENIUM_SERVER_PORT), "-browserTimeout", "120"]
            subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            # wait for nodes to register
            time.sleep(10)

    def _start_proxy_server(self):
        if not self._is_listening(self.config.ADDRESS, self.config.PROXY_SERVER_PORT):
            print "Proxy server seems not running. Trying to start on {0}:{1}...".format(self.config.ADDRESS, self.config.PROXY_SERVER_PORT)
            command = [self.config.PROXY_START_SCRIPT, "-port={0}".format(self.config.PROXY_SERVER_PORT)]
            subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def _is_listening(self, url, port):
        try:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.settimeout(1)
            socket_.connect((url, port))
            socket_.close()
            return True
        except socket.error:
            return False

    @property
    def proxy(self):
        return self._proxy

    @property
    def config(self):
        return self._config

    @property
    def desired_browser(self):
        return self._desired_browser

    @desired_browser.setter
    def desired_browser(self, browser):
        self._desired_browser = browser

    @property
    def active_driver(self):
        return self._active_driver

    @active_driver.setter
    def active_driver(self, driver):
        self._active_driver = driver

    @property
    def reporter_instance(self):
        return self._reporter_instance

    @reporter_instance.setter
    def reporter_instance(self, instance):
        self._reporter_instance = instance

    @property
    def test_loader(self):
        return self._test_loader

    @property
    def test_suite(self):
        return self._test_suite

swt = SeleniumWebtests()
