#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

a='100'
b=200
print a
print int(a)
print b
print str(b)
print len(a)
print type(b)


# 有用的内建函数
# 函数 描述
# dir([obj]) 显示对象的属性，如果没有提供参数， 则显示全局变量的名字                            
# help([obj]) 以一种整齐美观的形式 显示对象的文档字符串， 如果没有提供任何参
# 数， 则会进入交互式帮助。
# int(obj) 将一个对象转换为整数
# len(obj) 返回对象的长度
# open(fn, mode) 以 mode('r' = 读， 'w'= 写)方式打开一个文件名为 fn 的文件
# range([[ start ,] stop [, step ]) 返回一个整数列表。起始值为 start, 结束值为 stop - 1; start
# 默认值为 0， step默认值为1。
# raw_input(str) 等待用户输入一个字符串， 可以提供一个可选的参数 str 用作提示信
# 息。
# str(obj) 将一个对象转换为字符串
# type(obj) 返回对象的类型（返回值本身是一个 type 对象！）