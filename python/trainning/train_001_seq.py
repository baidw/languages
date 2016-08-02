#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

class Animal(object):
    """docstring for Animal"""
    
    def __init__(self,*args):
        self.param={}
        print list(args)
        
            # for k,v in args:
            #     self.param[k]=v

arg1=2
a=Animal(arg1)

