# -*- coding: utf-8 -*-

import socket

def is_listening(url, port):
    try:
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.settimeout(1)
        socket_.connect((url, port))
        socket_.close()
        return True
    except socket.error:
        return False
