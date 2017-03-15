#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: python_reportlab.py
__author__ = 'baidw'
import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.lib.pagesizes import letter, A4
# 注册中文字体库
pdfmetrics.registerFont(ttfonts.TTFont("msyh", "msyh.ttf"))

''' 
inspection_iterm_report:巡检项报告
'''


def inspection_iterm_report():
    rst = {}
    p = subprocess.Popen("ping www.baidu.com  -n 4",
                         shell=True, stdout=subprocess.PIPE)
    rst['ping www.baidu.com  -n 4'] = p.stdout.readlines()

    return rst


''' 

create_pdf:生成PDF文档

'''


def create_pdf(action, input, output="report.pdf"):
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    c = canvas.Canvas(output, pagesize=A4)

    c.addPageLabel(10)

    c.setFont('msyh', 10)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, 11 * inch)
    textobject.textLines('''%s''' % action)

    textobject.textLine(u'''执行时间:%s''' % date)
    textobject.textLine('-' * 60)

    for key in input:
        textobject.textLine(u'执行命令:[' + key.strip().decode('gb2312') + "]")
        textobject.textLine(u'执行结果如下：')
        for value in input[key]:
            textobject.textLine(value.strip().decode('gb2312'))

            if textobject.getY() == 0:

                c.drawRightString(4.2 * inch, textobject.getY(),
                                  u'Page:%s' % str(c.getPageNumber()))
                c.drawText(textobject)
                c.showPage()
                # print c.getPageNumber()
                c.addPageLabel(10)

                c.setFont('msyh', 10)
                textobject = c.beginText()
                textobject.setTextOrigin(inch, 11 * inch)
                textobject.textLine(text='')
        textobject.textLine('-' * 30)

    textobject.textLine('-' * 60)
    textobject.textLine('#' * 80)
    c.pageHasData()
    c.drawText(textobject)
    c.drawRightString(4.2 * inch, 0, u'Page:%s' % str(c.getPageNumber()))
    c.showPage()
    c.save()

'''
主程序入口
'''
if __name__ == '__main__':
    report = inspection_iterm_report()
    action = u'''
        XXXX系统巡检报告
巡检主机包括：
1.app-host1
2.app-host2
3.db-host1
4.db-host2
5.........
    '''
    create_pdf(action, input=report, output='x_report.pdf')
