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

class Runner(object):

    def __init__(self):

        self._config = config

        # include current directory into sys.path
        sys.path.append(os.getcwd())
        self._test_settings = __import__("settings")

        self._start_proxy_server()
        self._start_selenium_hub()

        self._proxy = None
        self._desired_browser = None
        self._active_driver = None

    def run(self):
        import reporter
        import testloader

        self._proxy = Proxy("{0}:{1}".format(self.config.IP, self.config.PROXY_SERVER_PORT))
        self._test_runner = unittest.TextTestRunner(verbosity=2, resultclass=reporter.Reporter)
        self._test_loader = testloader.TestLoader()
        print
        self._test_runner.run(self._test_loader.get_test_suite())
        self.end()

    def end(self):
        self._proxy.close()
        if self.active_driver:
            self.active_driver.quit()

    def _start_selenium_hub(self):
        if not self._is_listening(self.config.IP, self.config.SELENIUM_SERVER_PORT):
            print "Selenium HUB seems not running. Trying to start on {0}:{1}...".format(self.config.IP, self.config.SELENIUM_SERVER_PORT)
            command = ["java", "-jar", "{0}".format(self.config.SELENIUM_FILE), "-role", "hub", "-port", "{0}".format(self.config.SELENIUM_SERVER_PORT)]
            subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            # wait for nodes to register
            time.sleep(10)

    def _start_proxy_server(self):
        if not self._is_listening(self.config.IP, self.config.PROXY_SERVER_PORT):
            print "Proxy server seems not running. Trying to start on {0}:{1}...".format(self.config.IP, self.config.PROXY_SERVER_PORT)
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
    def test_settings(self):
        return self._test_settings

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

runner = Runner()
