#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def is_isogram(string):
    # string=string.upper()
    # str_tp=string
    # if len(string)==len(set(str_tp)):
    #     return True
    # else:
    #     return False
    return len(string) == len(set(string.lower()))
string='moOse'
x=is_isogram(string)
print x