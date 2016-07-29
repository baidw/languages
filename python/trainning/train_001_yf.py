#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

def get_count(words):
    v=['a','e','i','o','u']
    vcnt=0
    ccnt=0
    if isinstance(words,str):
        for w in words:
            if w.strip()=='':
                pass
            else:
                if w.lower() in v:
                    vcnt+=1
                else:
                    ccnt+=1
    return {"vowels":vcnt,"consonants":ccnt}

words='To Kata or not to Kata'
x=get_count(words)
print x
