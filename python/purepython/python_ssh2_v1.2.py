#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: python_ssh2_v1.2.py
__author__ = 'baidw'

import paramiko
import sys
import getpass


def ssh2(ip, port, uname, upass, cmds):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, uname, upass, timeout=5)
        for cmd in cmds:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            out = stdout.readlines()
            print '%s' % cmd
            for o in out:
                print o
        print 'ssh ip:%s and execute command finish.' % ip
        ssh.close()
        return 1
    except Exception, e:
        print 'ssh ip:%s failed.and Exception:' % (ip), e
        return 0

if __name__ == '__main__':
    ip = "localhost"
    port = 22
    login_name = ''
    login_pass = ''
    cmds = []

    arg0 = raw_input('Please input ip address(default:localhost):')
    if len(arg0) > 0:
        ip = arg0
    print ip
    try:
        arg1 = int(raw_input('Please input port(default:22):'))
        if len(arg1) > 0:
            port = int(arg1)
        print port
    except Exception, e:
        print port

    while True:
        arg2 = raw_input('Please input login name:')
        if len(arg2) > 0:
            login_name = arg2
            break
    print login_name

    while True:
        arg3 = getpass.getpass('Please input login password:')
        if len(arg3) > 0:
            login_pass = arg3
            break
    print login_pass

    while True:
        arg4 = raw_input('Please input cmd name(Escape character is "e"):')
        print arg4
        if str(arg4) == 'e':
            break
        elif len(arg4) > 0:
            cmds.append(arg4)
    print cmds
    
    flag = ssh2(ip, port, login_name, login_pass, cmds)
    # if flag:
    #     print 'login success and execute finish.'
    # else:
    #     print 'login ip failed or execute command failed.'
