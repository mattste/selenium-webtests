# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess
import socket
import unittest
import browsermobproxy

class Runner(object):

    def __init__(self):      

        # include current directory into sys.path
        sys.path.append(os.getcwd())
        self._settings = __import__("settings")
        self._start_selenium_hub()
        
        self._proxy_server = browsermobproxy.Server(self.settings.PROXY_START_SCRIPT, {"port": int(self.settings.PROXY_PORT)})        
        self._proxy = browsermobproxy.Client("{0}:{1}".format(self.settings.IP, self.settings.PROXY_PORT))
        self._desired_browser = None

    def run(self):
        import reporter
        import testloader

        self._test_runner = unittest.TextTestRunner(verbosity=2, resultclass=reporter.Reporter)
        self._test_loader = testloader.TestLoader()
        self._test_runner.run(self._test_loader.getTestSuite())
        self.proxy.close()

    def _start_selenium_hub(self):
        if not self._is_listening("localhost", int(self.settings.SELENIUM_SERVER_PORT)):
            stdout = open(os.devnull, 'w')
            command = ["java", "-jar", "{0}".format(self.settings.SELENIUM_FILE), "-role", "hub", "-port", "{0}".format(self.settings.SELENIUM_SERVER_PORT)]
            subprocess.Popen(command, stdout=stdout, stderr=subprocess.STDOUT)
            # wait for nodes to register
            time.sleep(5)

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
    def settings(self):
        return self._settings

    @property
    def desired_browser(self):
        return self._desired_browser

    @desired_browser.setter
    def desired_browser(self, browser):
        self._desired_browser = browser

runner = Runner()