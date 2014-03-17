#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import signal

from seleniumwebtests import swt

def signal_handler(signal, frame):
    print "\nKilling..."
    swt.end()
    sys.exit(0)

def main(options={}):
    signal.signal(signal.SIGINT, signal_handler)
    swt.setOptions(options)
    swt.run()

if __name__ == "__main__":
    main()

