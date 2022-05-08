#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 22:44:40 2022

@author: dantan
"""
#阶乘末尾如果包括0，因子一定包含5
def func(n):
    c=0
    while n/5>0:
        c+=int(n/5)
        n=int(n/5)
    return c
        
print(func(21))
print(func(25))



#传统耗时解法
def func(n):
    res=1
    for i in range(2,n+1):
        res*=i
    r=list(str(res))
    c=0
    while int(r[-1])==0 and len(r)>0:#注意数字类型
        c+=1
        r.pop()
    return c

print(func(21))
print(func(25))
