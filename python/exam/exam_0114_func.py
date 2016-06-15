#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def first_func():
	print 'This is my first function.'

def two_func(arg0):
	print 'This is my two function.arg0=',arg0
#函数的参数可以有一个默认值， 如果提供有默认值，在函数定义中， 参数以赋值语句的形式提供
def three_func(arg0=1):
	print 'This is my three function.arg0=',arg0

#调用函数方式
first_func()
two_func('hello')
three_func('hello')
three_func()

#def func_name([argx]):
#	func code block
#
#