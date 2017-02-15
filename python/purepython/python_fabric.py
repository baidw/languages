#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fabric.api import *
from fabric.colors import *

# env.hosts=['username@ip:port',]
# env.password = 'password'

env.roledefs = {
            'webserver':['username@ip:port'],
            'dbserver':['username@ip2:port','username@ip3:port'],
            }

env.passwords = {
 'username@ip:port': "password",
 'username@ip2:port': "password",
 'username@ip3:port': "password",
} 

def local_setting():
    local('echo "local prepare env."')

def remote_execute():
    print u'准备远程操作......'
    with cd('~/'):
        run('ulimit -n')

    print u'完成远程操作!'
    
@roles('webserver')   
def web_task():
    run("ps -ef|grep jboss")

@roles('dbserver')   
def db_task():
    run("ps -ef|grep oracle")

#服务器负载检查
@roles('webserver')
def server_uptime():
    s_uname=run('uname -a')
    s_osname=run('cat /etc/redhat-release')
    #服务器 持续在线时间days hours 用户数 最近1分钟内平均负载 最近5分钟内平均负载 最近15分钟内平均负载
    s_utime=run("uptime|awk '{print $3,$5,$6,$10,$11,$12}'|sed 's/\,//g'")

def dotask():
    execute(web_task)
    execute(db_task)
    execute(server_uptime)


#fab -f python_fabric.py dotask
