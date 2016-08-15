#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import os
import subprocess

def pingIp(target_ip):

    os_name = os.name
    os_type=("nt","dos","ce")
    ping_cmd='ping '

    if os_name=='posix':
        #print 'This is a linux os.'
        ping_cmd = ping_cmd +' -c 2 '
    elif os_name in os_type:
        #print 'This is a windows os.'
        ping_cmd = ping_cmd +' -n 2 '
    
    retcode= subprocess.call(ping_cmd + target_ip, shell=True)
    #retcode 0:代表成功; 非0:代表失败
    return retcode

if __name__ == '__main__':
    iplists=('www.baidu.com','hk.google.com')
    for iplist in iplists:
        rt=pingIp(iplist)
        if rt==0:
            print '%s is Alive.'%iplist 
        else:
            print '%s is Break.'%iplist
