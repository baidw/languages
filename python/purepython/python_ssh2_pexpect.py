#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: python_ssh2_pexpect.py
__author__ = 'baidw'
import pexpect


def ssh2(ip, name, passd, cmds):
    ret = -1
    ssh = pexpect.spawn('ssh %s@%s' % (name, ip))
    try:
        flag = ssh.expect(
            ['assword:', 'continue connecting (yes/no)?'], timeout=5)
        if flag == 0:
            ssh.sendline(passd)
        elif flag == 1:
            ssh.sendline('yes\n')
            ssh.expect('assword: ')
            ssh.sendline(passd)
        for cmd in cmds:
            ssh.sendline(cmd)
            r = ssh.read()
            print r

        ret = 0
    except pexpect.EOF:
        print 'EOF'
        ssh.close()
        ret = -1
    except pexpect.TIMEOUT:
        print 'TIMEOUT'
        ssh.close()
        ret = -2
    return ret

if __name__ == '__main__':
    ip = 'ip'
    name = 'username'
    passd = 'userpass'
    cmds = ['pwd', 'date', 'netstat -an|grep 22']
    print ssh2(ip, name, passd, cmds)
