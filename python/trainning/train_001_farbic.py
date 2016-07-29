#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'


def tribonacci(signature,n):
    #your code here
    temp = signature
    slen=len(temp)
    if n ==0:
        return []  
    if n==1 and len(list(set(signature)))==1:
        return signature[:1]
    while slen<n:
        temp.append(int(temp[slen-1])+int(temp[slen-2])+int(temp[slen-3]))
        slen=len(temp)
    
    return temp

x= tribonacci([1,1,1],1)
print x