#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import signal
from runner import runner

def signal_handler(signal, frame):
    print "\nKilling..."
    runner.end()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    runner.run()

if __name__ == "__main__":
    main()

