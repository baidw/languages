#!/usr/bin/env python
# -*- coding:utf-8 -*-
#filename: python_ftp.py
__author__ = 'baidw'
import ftplib



def ftp_cmd(ip, port, timeout, name, passd, cmds):
    ret =0
    ftp=None
    try:
        ftp = ftplib.FTP()
        ftp.connect(host=ip,port=port,timeout=timeout)
        ftp.login(user=name,passwd=passd)
    except ftplib.all_errors ,e:
        print e
        ftp.quit()
        ret=1
    
    try:
        print ftp.getwelcome()
        print ftp.cwd('/')

    except ftplib.all_errors,e:
        print e
        ftp.quit()
        ret=1

    print "="*20

    try:
        lines= ftp.retrlines('LIST')
        for l in lines:
            print l
        print '='*20    
    except ftplib.all_errors ,e :
        print e 
        ftp.quit()   
        ret =1
    ftp.quit() 
    return ret

if __name__ == '__main__':
    ip='ip'
    port=21
    timeout=5
    name='user'
    passd='password'
    cmds=['LIST']
    ftp_cmd(ip,port,timeout,name,passd,cmds)

    
