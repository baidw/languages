#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

#one comment
#two comment

def mymaxnum(a,b):
	"this is a compare b ,if a>b return a,else return b "
	if a>b:
		return a
	else:
		return b

print "max number:",mymaxnum(10,20)
print "文档字符串注释[用于在线文档]:",mymaxnum.__doc__

