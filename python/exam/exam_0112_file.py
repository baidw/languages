#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

fhandle=open('exam_0101_hello.py',mode='r')

for eachLine in fhandle:
	print eachLine
fhandle.close()

 #mode 中 'r' 表示读取，'w' 表示写入， 'a' 表示添加。
 #其它可能用到的标声还有 '+' 表示读写， 'b'表示二进制访问. 
 #如果未提供 mode ， 默认值为 'r'。如果 open() 成功， 一个文件对象句柄会被返回。


 #什么是属性？
#属性是与数据有关的项目， 属性可以是简单的数据值， 也可以是可执行对象， 比如函数和方法。
#哪些对象拥有属性呢？ 很多。 类， 模块， 文件还有复数等等对象都拥有属性。
#我如何访问对象属性？ 使用句点属性标识法。 也就是说在对象名和属性名之间加一个句点： object.attribute