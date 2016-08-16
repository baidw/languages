#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import os
import subprocess
import socket

def pingIp(target_ip):

    os_name = os.name
    os_type=("nt","dos","ce")
    ping_cmd='ping '

    if os_name=='posix':
        #print 'This is a linux os.'
        ping_cmd = ping_cmd +' -c 1 '
    elif os_name in os_type:
        #print 'This is a windows os.'
        ping_cmd = ping_cmd +' -n 1 '
    
    retcode= subprocess.call(ping_cmd + target_ip, shell=True)
    #retcode 0:代表成功; 非0:代表失败
    return retcode

def scanPort(target_ip,target_port):
    isOpen=False
    rt=pingIp(target_ip)
    if rt==0:
        st = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        st.settimeout(1)
        try:
            st.connect((target_ip,target_port))
            isOpen=True
            print "%s's %d port is open."%(target_ip,target_port)
        except Exception :
            isOpen=False
            print "%s's %d port is closed."%(target_ip,target_port)
        st.close()
    else:
        isOpen=False
        print "%s's %d port is closed."%(target_ip,target_port)
    return isOpen
if __name__ == '__main__':
    iplists=('www.baidu.com','hk.google.com','www.sina.com','www.sohu.com')
    for iplist in iplists:
        rt=pingIp(iplist)
        if rt==0:
            print '%s is Alive.'%iplist 
            for i in xrange(79,85):
                scanPort(iplist,i)
        else:
            print '%s is Break.'%iplist
