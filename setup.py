# -*- coding: utf-8 -*
"""
Selenium-webtests installation script.

USAGE:
python setup.py install
"""

import platform
import json
from setuptools import setup

print "Installing selenium-webtests..."
print
conf = {}
conf["IP"] = raw_input("This machine IP: ")
conf["SELENIUM_FILE"] = raw_input("Path to selenium standalone server .jar file: ")
conf["SELENIUM_SERVER_PORT"] = raw_input("Selenium server port [4444]:") or 4444
conf["PROXY_START_SCRIPT"] = raw_input("Path to the browsermob-proxy start file (.sh or .bat): ")
conf["PROXY_PORT"] = raw_input("Proxy server port [3128]: ") or 3128

f = open('seleniumwebtests/config.py', 'w+')
f.write('conf = ' + repr(conf) + '\n' )
f.close()

script = "scripts/runwebtests"
if platform.system() == "Windows":
    script = "scripts/runwebtests.cmd"

setup(
    name = 'seleniumwebtests',
    packages = ['seleniumwebtests'],
    version = '0.1',
    description = '',
    author = 'Jiri Kuchta',
    author_email = 'jiri.kuchta@live.com',
    url = 'https://github.com/jirikuchta/selenium-webtests',
    keywords = ['testing', 'selenium'],
    install_requires=[
        'selenium>=2.38.4',
        'browsermob-proxy>=0.6.0',
    ],
    scripts=[script],
)
