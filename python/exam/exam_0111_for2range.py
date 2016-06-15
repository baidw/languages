#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'baidw'

for iterm in ['hello', 'python', 'world']:
    print iterm

for iterm in range(5):
    print iterm

for iterm in 'abc':
    print iterm
# range()函数经常和 len()函数一起用于字符串索引
strs = 'abc'
for i in range(len(strs)):
    print strs[i], '(%d)' % i
# 直接得到索引及其元素
for i, v in enumerate(strs):
    print v, '(%d)' % i

# 列表解析甚至能做更复杂的事情
sqrd = [x**2 for x in range(10) if not x % 2]
for i in sqrd:
    print i
