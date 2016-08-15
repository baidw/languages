#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import urllib2
url="https://zhuanlan.zhihu.com/p/21839027"
#data = {'data1':'XXXXX', 'data2':'XXXXX'}
#data = urllib.urlencode(data)
#full_url = url+'?'+data


response = urllib2.urlopen(url)
content=urllib2.urlopen(url).read()
print "response headers:",response.headers
print "content:",content

