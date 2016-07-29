#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def high_and_low(numbers):
    nlist=numbers.split(' ')
    print nlist
    #return "%d %d"%(max(list(numbers)),min(list(numbers)))

numbers="4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
x = high_and_low(numbers)
print x