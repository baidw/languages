#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

try:
	filename=raw_input('Enter your file name:')
	fhandle=open(filename,'r')
	for eachLine in fhandle:
		print eachLine
	fhandle.close()
except IOExcept ,e :
	print 'File open error.',e

