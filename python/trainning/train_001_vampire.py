#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def vampire_test(x, y):
    if x<=0 and y<=0:
        return False
    strx=abs(x)
    stry=abs(y)
    strxy=abs(x)*abs(y)
    xlen=len(str(strx))
    ylen=len(str(stry))
    ustr=str(strx)+str(stry)
    tlen=xlen+ylen
    slen=len(str(strxy))
    rtn=False
    st=(list(str(strxy)))
    ut=(list(ustr))
    st.sort()
    ut.sort()
    print st,ut

    if tlen==slen:
        for ii in range(tlen):
            if st[ii]==ut[ii]:
                pass
            else:
                return False
        for x in str(strxy):
            if x not in ustr:
                return False
            else:
                rtn=True
    else:
        return False
    return rtn 
    #print xlen,ylen
    # rt=abs(x)*abs(y)
    # strx=list(str(x))
    # stry=list(str(y))
    # rtstr=list((strx+stry))
    # mstr=list((str(rt)))
    # rtn=False

    # if len(rtstr)==len(mstr):
    #     for x in mstr:
    #         if x not in rtstr:
    #             rtn=False
    #             return rtn
    #         else:
    #             rtn=True
    # else:
    #     rtn=False            
    # return rtn
x=2947051 
y=8469153 
print x*y
a =vampire_test(x,y)
print a