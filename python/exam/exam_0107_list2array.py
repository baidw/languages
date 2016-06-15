#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

#List
aList=[1,2,3,4,5]
bList=[1,'2',True,3.14,1l]
#Tuple
aTuple=(1,2,3,4,5)
bTuple=(1,'2',True,3.14,1l)

print aList
print bList
print aList[2:]
aList[2]=10
print aList

print aTuple
print bTuple
print aTuple[2:]
#元组也可以进行切片运算，得到的结果也是元组（不能被修改）
#无法执行:aTuple[2]=10

#列表和元组可以存储不同类型的对象 
#列表元素用中括号( [ ])包裹，元素的个数及元素的值可
#以改变。元组元素用小括号(( ))包裹，不可以更改（尽管他们的内容可以）。
#元组可以看成是只读的列表。通过切片运算( [ ] 和 [ : ] )可以得到子集，
#这一点与字符串的使用方法一样