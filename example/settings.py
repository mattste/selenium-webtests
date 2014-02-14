# -*- coding: utf-8 -*-

# this machine IP
# Machine has to be accesible on this address from the nodes
IP = "192.168.56.1"

# path to the selenium standalone server file (.jar)
# (download at http://code.google.com/p/selenium/downloads/list)
SELENIUM_FILE = "/home/jk/Downloads/selenium/selenium-server-standalone-2.39.0.jar"

# port to run the selenium server hub on
SELENIUM_SERVER_PORT = 4444

# path to browsermob-proxy start file
# (download at http://bmp.lightbody.net/)
PROXY_START_SCRIPT = "/home/jk/Downloads/selenium/browsermob-proxy/bin/browsermob-proxy"

# port to run the proxy server on
PROXY_SERVER_PORT = 3128

BASE_URL = "http://zbozi.cz"

BROWSERS = [
    {
        "browserName": "firefox",
        "version": "ANY",
        "platform": "ANY"
    }
]
