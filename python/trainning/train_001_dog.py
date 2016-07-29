#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

# TODO: solve the barking problem!
class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age
        
    def bark(self):
        return 'Woof!'

d=Dog(name='asdf',breed='bread',sex='male',age=6)
print d.bark()