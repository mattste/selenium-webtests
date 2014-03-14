# -*- coding: utf-8 -*
"""
Selenium-webtests installation script.

USAGE:
python setup.py install
"""

from setuptools import setup

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
        'unittest-xml-reporting>=1.7.0'
    ],
    scripts=["bin/runwebtests.cmd","bin/runwebtests"],
)
