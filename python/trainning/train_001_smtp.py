#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import smtplib
from email.mime.text import MIMEText 

mail_host = 'smtp.163.com'
mail_port = 25
mail_timeout= 5
mail_user = "uname"
mail_pass = "pass"
mail_postfix="163.com" 
mail_login_user = mail_user+"@"+mail_postfix
me = mail_user + "<"+mail_user+"@"+mail_postfix+">" 

def sendEmail(to_addr,msg):
    try:
        smtp=smtplib.SMTP(host=mail_host, port=mail_port, timeout=mail_timeout)
        smtp.login(user=mail_login_user, password=mail_pass)
        smtp.sendmail(from_addr=me, to_addrs=to_addr, msg=msg, mail_options='')
        smtp.close()
        print "Successfully sent email!"
        return True
    except Exception,e:
        print str(e)
        print "Error: unable to send email"
        return False

if __name__ == '__main__':
    sendEmail(["mail_user@163.com"],"hello")
    