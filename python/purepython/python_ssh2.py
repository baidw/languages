#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: python_ssh2.py
__author__ = 'baidw'

import paramiko


def ssh2(ip, port, uname, upass, cmds):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, uname, upass, timeout=5)
        for cmd in cmds:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            out = stdout.readlines()
            print '%s'%cmd
            for o in out:
                print o
        print 'ssh ip:%s and execute command finish.'%ip
        ssh.close()
        return 1
    except Exception, e:
        print 'ssh ip:%s failed.and Exception:'%(ip),e
        return 0


if __name__ == '__main__':
    ip = "ip"
    port = 22
    login_name = 'login_name'
    login_pass = 'login_pass'
    cmds = ['netstat -an|grep 22', 'date']
    flag=ssh2(ip, port, login_name, login_pass, cmds)
    if flag:
        print 'login success and execute finish.'
    else:
        print 'login ip failed or execute command failed.'