#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

#3位数字，水仙数算法
for i in range(100,1000):
    sum = 0 
    temp = i 
    while temp:
        sum += (temp%10)**3
        temp //=10   #地板除 ，即：temp = temp//10  
        #执行地板除://除法不管操作数为何种数值类型,总是会舍去小数部分
    if sum == i:
        print i 

