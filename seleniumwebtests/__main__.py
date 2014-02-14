#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import signal
from runner import runner

def signal_handler(signal, frame):
    print "Killing..."
    runner.end()
    sys.exit(0)

def main():
    runner.run()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()

