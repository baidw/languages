#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def Descending_Order(num):
    # if num:
    #     strNum=str(num)
    #     strList=[]
    #     maxList=""
    #     for i in (strNum):
    #         strList.append(i)
    #     strList.sort()
    #     strList.reverse()
    #     print strList
    #     for s in strList:
    #         maxList +=s
    #     if maxList=="" :
    #         return 0
    #     return int(maxList)
    # else:
    #      return 0
    return int("".join(sorted(str(num), reverse=True)))
num=1201
x=Descending_Order(num)
print x         