#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'
import sys
#提示信息
banners='''
============================================
|iterm   comment                           |
|1       get  all numbers  sum             |
|2       get  all numbers  avg             |
|3       list all numbers                  |
|0        exit (and other input numbers.)  |
============================================
'''

selectIterm=[1,2,3,]
inpdata=[1,2,3,4,5,6,7,8,9,10]
#求和
def sum_func(inparam):
    sum_o=0
    for i in inparam:
        sum_o+=i
    return sum_o
#求均值
def avg_func(inparam):
    avg_o=0;
    inparam_len=len(inparam)
    cnt =sum_func(inparam)
    return (cnt/inparam_len)
#查看数据
def list_func(inparam):
    return inparam
#退出
def exit_func():
    sys.exit()

calIterm={1:sum_func,2:avg_func,3:list_func}
strText=0
#循环
while True:
    print banners
    strText =raw_input("enter a number:")
    #判断是否为数字，非数字直接退出    
    if not str(strText).isdigit():
        print "your enter is not digit,exit!"
        exit_func()
    else:
        intText=int(strText)
        if intText in selectIterm:
            for s in selectIterm:
                if intText ==s:
                    #调用对应的函数，并打印返回值
                    print calIterm.get(intText)(inpdata)
        else:
            print "no this iterm ,exit!"
            exit_func()
