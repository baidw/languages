#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def producer():
    r = yield 1
    print('producer get:',r)
    r = yield 2
    print(r)
    r = yield 3
    print(r)
    
def consumer(gen):
    t =  next(gen)
    print(t)
    temp = 10
    while True:
        try:
            t = gen.send(temp)
            print('consumer receive:',t)
            temp += 1
        except StopIteration:
            return

consumer(producer())