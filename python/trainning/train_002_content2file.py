#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

wordlist = ['hello','python','world.']
namelist = ['1.txt','3.txt','5.txt']

for i in range(len(wordlist)):
    #print wordlist[i],namelist[i]
    f = open(namelist[i], "w" )  
    f.write(wordlist[i])  
    f.close() 