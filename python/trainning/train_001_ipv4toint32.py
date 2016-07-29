#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def ip_to_int32(ip):
    #print np.int32(ip)
    # ips=ip.split(".")
    # ipi=[bin(int(x)).replace('0b','') for x in ips]
    # ipa=''
    # for i in ipi:
    #     l=len(i)
    #     if l<8:
    #         ipa+=(('0'*(8-l))+i)
    #     else:
    #         ipa+=i

    # ipa='0b'+ipa
    # return int(ipa,2)
    ips=ip.split('.')
    res=int(ips[0])<<24
    res+=int(ips[1])<<16
    res+=int(ips[2])<<8
    res+=int(ips[3])
    return res



x=ip_to_int32("128.32.10.1")
print x