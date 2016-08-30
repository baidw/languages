#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'


import netifaces
import socket

def getLocalLink():
    rtnLinks=[]
    for infs in netifaces.interfaces():
        addrs =netifaces.ifaddresses(infs)
        for x in addrs.items():
            #print x
            if x[0] == netifaces.AF_LINK:
                rtnLinks.append(x[1])
    return  rtnLinks

def getLocalInet():
    rtnInets=[]
    for infs in netifaces.interfaces():
        addrs =netifaces.ifaddresses(infs)
        for x in addrs.items():
            #print x
            if x[0] == netifaces.AF_INET:
                rtnInets.append(x[1])
    return  rtnInets

def getLocalInet6():
    rtnInets6=[]
    for infs in netifaces.interfaces():
        addrs =netifaces.ifaddresses(infs)
        for x in addrs.items():
            #print x
            if x[0] == netifaces.AF_INET6:
                rtnInets6.append(x[1])
    return  rtnInets6

def getDefaultGateway():
    #获取默认网关
    gws = netifaces.gateways()
    gwslist=gws['default'][netifaces.AF_INET]
    return gwslist

def getHostname():
    hname=socket.gethostname()
    return hname

def getLocalip():
    hname=socket.gethostname()
    ip = socket.gethostbyname(hname)  
    return ip

def getExtendHostinfo():
    hname=socket.gethostname()
    ipList = socket.gethostbyname_ex(hname) 
    return ipList

if __name__ == '__main__':
    #print netifaces.interfaces()
    # for infs in netifaces.interfaces():
    #     addrs =netifaces.ifaddresses(infs)
    #     for x in addrs.items():
    #         #print x
    #         if x[0] == netifaces.AF_LINK:
    #             print 'LINK:',x[1]
    #         elif x[0] == netifaces.AF_INET:
    #             print 'INET:',x[1]
    #         elif x[0] == netifaces.AF_INET6:
    #             print 'INET6:',x[1]
    #         else:
    #             print 'OTHER:',x
    
    # print netifaces.AF_LINK
    # print netifaces.AF_INET
    # print netifaces.AF_INET6

    # #获取默认网关
    # gws = netifaces.gateways()
    # gwslist=gws['default'][netifaces.AF_INET]
    # print 'default gateways:',gwslist[0]
    # print 'default gateways address families:',gwslist[1]
    

    #print getLocalLink()
    #print getLocalInet()
    #print getLocalInet6()
    #print getDefaultGateway()
    print getHostname()
    print getLocalip()
    print getExtendHostinfo()