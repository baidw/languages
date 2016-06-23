#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'baidw'

import os
import subprocess

os_name = os.name

os_type = ("nt", "dos", "ce")

ping_cmd = 'ping '
# 判断系统的类型,确定ping的参数
if os_name == 'posix':
    print 'This is linux os system.'
    ping_cmd = ping_cmd + ' -c 2 '
elif os_name in os_type:
    print 'This is window os system.'
    ping_cmd = ping_cmd + ' -n 2 '
# ping ip列表
ping_list = ('192.168.1.1', 'www.baidu.com')
# 执行循环读取ping ip列表，确定是否通
for pingip in ping_list:
    # 调用ping命令
    rn = subprocess.call(ping_cmd + pingip, shell=True)
    # ping 返回的状态码,0代表成功
    if rn == 0:
        print '%s is Alive.' % (pingip)
    else:
        print '%s is Break.' % (pingip)
