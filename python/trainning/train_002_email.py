#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import smtplib
from email.mime.text import MIMEText

receiver_lists=['125113435@qq.com']    #收件人(列表)
sender_mail_host='smtp.163.com'              #发送邮件的smtp服务器地址,比如163
sender_mail_port=25
sender_name='mail_user'                 #发送邮件的用户
sender_pass='mail_pass'                 #发送邮件的密码
sender_postfix='163.com'                #邮箱后缀，比如163邮箱后缀
#发送邮件--只发送文本方式的邮件
def send_mails(mail_sendlists,mail_subject,mail_content):
    msg = MIMEText(mail_content,_subtype='plain')
    msg['Subject'] = mail_subject
    from_lists="<"+sender_name+"@"+sender_postfix+">"
    msg['From'] =from_lists
    msg['To'] = ";".join(mail_sendlists)
    
    try:
        sm = smtplib.SMTP()
        sm.connect(sender_mail_host,sender_mail_port)
        sm.login(sender_name,sender_pass)
        sm.sendmail(from_lists,mail_sendlists,msg.as_string())
        sm.close()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__ == '__main__':
    isFlag=send_mails(receiver_lists,'email subjects','email contents')
    if isFlag:
        print '邮件发送成功'
    else:
        print '邮件发送失败'

