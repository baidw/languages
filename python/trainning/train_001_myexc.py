#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'
  
if __name__ == "__main__":
    #main()
    #判断一个串是什么类型的，然后根据类型做转换，如果类型是unicode
    #用s.decode('gbk')会将字符串内容转换为中文
    s=u'\u4e0e\u4e16\u754c\u5206\u4eab\u4f60\u7684\u77e5\u8bc6\u3001\u7ecf\u9a8c\u548c\u89c1\u89e3'
    print type(s)
    print s.decode('gbk')
