#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import os
import subprocess
import socket
import threading

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

def checkIpPort(target_ip,target_ports):
    #判断是否能ping通ip
    if pingIp(target_ip)==0:
        print '%s is Alive.'%target_ip 
        #ping通的IP地址，则扫描port
        for target_port in target_ports:
            scanPort(target_ip, target_port)

    else:
        #ping不通的IP直接输出IP地址
        print '%s is Break.'%target_ip

if __name__ == '__main__':
    #iplists=('www.baidu.com','hk.google.com','www.sina.com','www.sohu.com')
    iplists=('192.168.0.1',)
    portlists=(21,22,23,25,37,53,69,70,80,110,119,137,138,139,143,161,162,389,443,445,636,1080,1433,1434,1521,1701,1723,3306,3389,5000,8000,8080,)
    threads=[]

    for iplist in iplists:
        threads.append(threading.Thread(target=checkIpPort,args=(iplist,portlists,)))
        
    for t in threads:
        #将线程声明为守护线程,必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
        t.setDaemon(True)
        #开始线程活动
        t.start()
        #在子线程完成运行之前，子线程的父线程将一直被阻塞
        t.join()
