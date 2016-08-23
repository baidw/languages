#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'


def generator_func():
    for i in range(5):
        print i 

def generator_func2():
    for i in range(5):
        return i 

def generator_func3():
    for i in range(5):
        yield i 

x0=generator_func()
print x0
print '========='
x1=generator_func2()
print x1
print '========='
x2=generator_func3() 
for i in x2:
    print i
print '========='


