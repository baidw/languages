#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: python_urllib_demo.py
__author__ = 'baidw'
import urllib


if __name__ == '__main__':
    url = 'http://www.baidu.com?'
    # urlopen()打开一个页面
    response = urllib.urlopen(url)
    html = response.read()
    # print html

    values = {'wd': 'python', 'pn': '30'}
    # urlencode()将key-value形式 转换为 “wd=python&pn=30” 字符串形式
    data = urllib.urlencode(values)
    print data
    print url + data

    s = '学习'
    # 对字符进行encode转换，则直接可以是quote()
    encodes = urllib.quote(s)
    print encodes
    # 通过decode()解码
    uq = urllib.unquote(encodes)
    decodes = uq.decode('utf-8')
    print decodes
