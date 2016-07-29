#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def find_it(seq):
    cnt=0
    for s in list(set(seq)):
        if s>0:
            if s%2 == 0:
                pass
            else:
                cnt+=1              
        else:
            cnt+=1
    if seq == None:
        return -1
    return cnt

seq=[20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
x=find_it(seq)
print '--->',x