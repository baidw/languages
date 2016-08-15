#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import requests

url="https://zhuanlan.zhihu.com/p/21839027"
response = requests.get(url)
content= requests.get(url).content
print "response headers:",response.headers
print "content:",content
