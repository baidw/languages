#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import requests
from bs4 import BeautifulSoup

url='https://www.baidu.com'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
r=requests.get(url,headers=headers)
#print r.status_code

print r.content.decode('gbk','ignore')
# soup = BeautifulSoup(r.content.decode('gbk','ignore'))
# stras=soup.find_all('<a')
# for stra in stras:
#     href=stra.get('href')
#     print href
