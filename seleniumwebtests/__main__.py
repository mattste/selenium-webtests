#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import signal
from runner import runner

def signal_handler(signal, frame):
    runner.proxy_server.close()
    sys.exit(0)

def main():
    runner.run()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()

