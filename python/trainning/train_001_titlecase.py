#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'


def title_case(title, minor_words=''):
    strL=title.split(' ')
    strL=[strl.lower() for strl in strL]
    miwL=minor_words.split(' ')
    miwL=[strm.lower() for strm in miwL]
    
    for i in range(len(strL)):
        if i==0:
            t=strL[i]
            strL[i]=strL[i][0].upper()+t[1:]
        else:
            if strL[i].lower() in miwL:
                strL[i]=strL[i].lower()
            else:
                te=strL[i]
                strL[i]=strL[i][0].upper()+te[1:]
    return str(' '.join(strL))


print title_case('a clash of KINGS','a an the of')
print title_case('THE WIND IN THE WILLOWS','The In')