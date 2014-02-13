#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import unittest
import seleniumwebtests as swt

proxy_server = None
test_runner = unittest.TextTestRunner(verbosity=2, resultclass=swt.Reporter)
test_loader = swt.TestLoader()
swt.myglobals.proxy = swt.Proxy()

def main():
    # include current directory into sys.path
    sys.path.append(os.getcwd())

    # save the test settings into globals
    swt.myglobals.settings = __import__("settings")

    if not swt.utils.is_listening("localhost", int(swt.config.SELENIUM_SERVER_PORT)):
        stdout = open(os.devnull, 'w')
        command = ["java", "-jar", "{0}".format(swt.config.SELENIUM_FILE), "-role", "hub", "-port", "{0}".format(swt.config.SELENIUM_SERVER_PORT)]
        subprocess.Popen(command, stdout=stdout, stderr=subprocess.STDOUT)
        # wait for nodes to register
        time.sleep(5)

    # run the tests
    test_runner.run(test_loader.getTestSuite())

    swt.myglobals.proxy.stop()

class Mytest():

    def __init__(self):
        self.var = "Ahoj"

if __name__ == "__main__":
    main()
