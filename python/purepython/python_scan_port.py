#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: python_scan_port.py
__author__ = 'baidw'
import os
import commands


def scan_ip_port(ips, ports):
    pass


def concat_cmd(ips, ports, cmd):
    cmds = []
    for ip in ips:
        for p in ports:
            cmds.append(cmd + ' ' + ip + ' ' + str(p))
    return cmds
if __name__ == '__main__':
    ips = ['www.baidu.com']
    ports = ['']
    cmd = concat_cmd(ips, ports, 'ping')
    print os.getcwd()
    for c in cmd:
        print c
        outlines = os.popen(c).readlines()
        print outlines
