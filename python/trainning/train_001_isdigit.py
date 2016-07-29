#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def validate_pin(pin):
    if (len(pin) not in (4,6)):
        return False
    else:
        return pin.isdigit()

pin='1234'
x= validate_pin(pin)
print x