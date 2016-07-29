#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def iq_test(numbers):
    nlist=numbers.split(' ')
    odd=0
    od=[]
    even=0
    ev=[]
    for x in range(0,len(nlist)):
        if int(nlist[x])%2==0:
            odd+=1
            od.append(x)
        else:
            even+=1
            ev.append(x)
        if odd+even>2:
            if odd>even:
                return  ev[0]+1
            else:
                return od[0]+1

numbers="2 4 7 8 10"
#numbers="1 2 2"
x=iq_test(numbers)
print x