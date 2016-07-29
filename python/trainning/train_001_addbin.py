#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def add_binary(a,b):
    return bin(int(a+b)).replace('0b','')

a=100
b=23
x = add_binary(a,b)
print x