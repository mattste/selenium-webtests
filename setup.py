# -*- coding: utf-8 -*
"""
Selenium-webtests installation script.

USAGE:
python setup.py install
"""

import platform
import os
from setuptools import setup

print "Installing selenium-webtests..."
print

#------------------------------------------------------------------------------
# Getting configuration
#------------------------------------------------------------------------------
config = {}
config["IP"] = raw_input("\033[95mThis machine IP:\033[0m\n") or '192.168.56.1'
config["SELENIUM_FILE"] = raw_input("\033[95mPath to selenium standalone server .jar file:\033[0m\n\
(download at https://code.google.com/p/selenium/downloads/list)\n") or '/home/jk/Downloads/selenium/selenium-server-standalone-2.39.0.jar'
config["SELENIUM_SERVER_PORT"] = raw_input("\033[95mSelenium server port [4444]:\033[0m\n") or 4444
config["PROXY_START_SCRIPT"] = raw_input("\033[95mPath to the browsermob-proxy start file (.sh or .bat):\033[0m\n\
(download at http://bmp.lightbody.net/)\n") or '/home/jk/Downloads/selenium/browsermob-proxy/bin/browsermob-proxy'
config["PROXY_PORT"] = raw_input("\033[95mProxy server port [3128]:\033[0m\n") or 3128

# write the configuration into file
if os.path.exists('seleniumwebtests/config.py'):
    os.remove('seleniumwebtests/config.py')
f = open('seleniumwebtests/config.py', 'a')
for key in config:
    f.write(key + " = '" + str(config.get(key)) + "'" + '\n')
f.close()

"""
TODO: windows run script
script = "scripts/runwebtests"
if platform.system() == "Windows":
    script = "scripts/runwebtests.cmd"
"""

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
    scripts=["scripts/runwebtests"],
)
