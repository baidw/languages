#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: python_pc_info.py
__author__ = 'baidw'
import socket
import os

if __name__ == '__main__':
    pc_name = socket.gethostname()
    print 'Your PC Name:', pc_name

    os_name = os.name
    os_type = ('nt', 'dos', 'ce')

    if os_name == 'posix':
        print 'This is a linux os.'
    elif os_name in os_type:
        print 'This is a window os.'
    else:
        print 'This is a other os.'
    