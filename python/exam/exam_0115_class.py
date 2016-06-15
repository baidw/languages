#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

class FirstClass(object):
	"""This is my first class"""
	def __init__(self,arg0='python'):
		super(FirstClass,self).__init__()
		self.name=arg0

	def showname(self):
		print self.name

#		
firstinstance=FirstClass()
firstinstance.showname()
firstinstance=FirstClass('hello')
firstinstance.showname()

# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg
		

#类是面向对象编程的核心， 它扮演相关数据及逻辑的容器角色。
#它们提供了创建“真实”对象(也就是实例)的蓝图

#当一个类实例被创建时， __init__() 方法会自动执行， 
#在类实例创建完毕后执行， 类似构建函数。
#__init__() 可以被当成构建函数， 不过不象其它语言中的构建函数， 
#它并不创建实例--它仅仅是你的对象创建后执行的第一个方法

#什么是 self ? 它是类实例自身的引用。其他语言通常使用一个名为 this 的标识符
