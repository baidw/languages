#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'baidw'

aDict = {1: "1", 2: 2, 3: 3.14, 4: True}
print aDict
print aDict[1]
print aDict.keys()
for key in aDict:
    print key, aDict[key]
print '-' * 5
for k, v in aDict.items():
    print k, v
# 字典是 Python 中的映射数据类型,字典元素用大括号({ })包裹
