#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def remove_smallest(numbers):
    # cnt=0;
    # lenN=len(numbers)
    # if lenN<=0:
    #     return []
    # numbers.pop(numbers.index(min(numbers)))
    # return numbers
    if numbers:
        numbers.remove(min(numbers))
    return numbers
    
    #raise NotImplementedError("Wrong result for "+str(numbers))
    

x=remove_smallest([1,2,3,4,3,2,1,4,76])
print x
