#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import socket

HOST = '136.224.243.185'
PORT = 1 

s = socket.socket(socket.AF_INET,socket.SOCK_RAW)
s.connect((HOST,1))
s.sendall('echo')
data=s.recv(1024)
s.close()
print data