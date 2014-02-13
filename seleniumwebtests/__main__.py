#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import socket
import unittest
import browsermobproxy

from seleniumwebtests import config
from seleniumwebtests import testloader
from seleniumwebtests import reporter
from seleniumwebtests import myglobals

proxy_server = None
test_runner = unittest.TextTestRunner(verbosity=2, resultclass=reporter.Reporter)
test_loader = testloader.TestLoader()

def is_selenium_grid_hub_running():
    """
    Method to test whether Selenium Grid HUB is running
    on localhost port specified in the config file
    """
    try:
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.settimeout(1)
        socket_.connect(("localhost", int(config.SELENIUM_SERVER_PORT)))
        socket_.close()
        return True
    except socket.error:
        print "Selenium Grid Hub does not running. Try execute \"java -jar {0} -role hub\".".format(config.SELENIUM_FILE)
        sys.exit()


def start_proxy():
    """
    Starts the browsermob-proxy server and client
    The client is passed to the testcase so we can use it in our tests
    """
    global proxy_server
    proxy_server = browsermobproxy.Server(config.PROXY_START_SCRIPT, {"port": int(config.PROXY_PORT)})
    proxy_server.start()
    myglobals.proxy = browsermobproxy.Client("{0}:{1}".format(config.IP, config.PROXY_PORT))


def main():
    # include current directory into sys.path
    # in order to be able to import files from there
    sys.path.append(os.getcwd())

    myglobals.settings = __import__("settings")

    is_selenium_grid_hub_running()
    start_proxy()
    test_runner.run(test_loader.getTestSuite())
    proxy_server.stop()


if __name__ == "__main__":
    main()
