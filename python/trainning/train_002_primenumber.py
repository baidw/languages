#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import math

def isPrimeNumber(x):
    cnt=0
    for i in range(2,x+1):
        if x%i==0:
            cnt+=1
            if cnt >1:
                break
    if cnt>1:
        return False
    else:
        return True

def champion(x=10):
    retResult=[]
    if x<2:
        return retResult
    else:
        for i in xrange(2,x+1):
            #判断是否是素数
            if isPrimeNumber(i):
                retResult.append(i)
    return retResult

if __name__ == '__main__':
    print champion()
    print champion(50)
    for i in champion(100):
        print i,