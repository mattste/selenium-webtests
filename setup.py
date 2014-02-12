# -*- coding: utf-8 -*
"""
Selenium-webtests installation script.

USAGE:
python setup.py install
"""

from setuptools import setup

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
