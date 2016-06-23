#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'
import os, sys

#定义查找和替换文本的方法
#stext 查找的内容
#rtext 替换的内容
#infile  原文件
#outfile 输出文件
def search_replace_text(stext,rtext,infile,outfile):
  try:
    #按行读取原文件
    for c in infile:
      #查找文件，并替换内容，输出到新文件中
      outfile.write(c.replace(stext,rtext))
    return True
  except Exception ,ex:
    print ex
  return False

if __name__ == '__main__':
  #获取执行命令时，传参的数量
  nargs = len(sys.argv)
  #判断参数是否为
  if not 3 <= nargs <= 5:
    print('usage: %s search_text repalce_text [infile [outfile]]' % \
       os.path.basename(sys.argv[0]))
  else:
    search_text = sys.argv[1]
    replace_text = sys.argv[2]
    input_file = sys.stdin
    output_file = sys.stdout
    if nargs > 3:
      input_file = open(sys.argv[3])
    if nargs > 4:
      output_file = open(sys.argv[4], 'w')
    srflag=search_replace_text(search_text,replace_text,input_file,output_file)
    if srflag:
      print 'open %s file,find "%s" and replace for "%s" ,to output %s file.'%(sys.argv[3],search_text,replace_text,sys.argv[4])
    #关闭文件
    output_file.close()
    input_file.close()
#python train_001_replacetext.py 查找内容 替换内容 原文件 输出文件
#python train_001_replacetext.py search_text replace_text source_file output_file
