#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:11:37 2022

@author: dantan
"""
20//6 # 2
20%6  # 3

1//6 # 0 

# 1134
#假设存在一个 k 位数 N，其每一位上的数字的 k 次幂的总和也是 N，那么这个数是阿姆斯特朗数。
# 给你一个正整数 N，让你来判定他是否是阿姆斯特朗数，是则返回 true，不是则返回 false。
# EG：153 是一个 3 位数，且 153 = 1^3 + 5^3 + 3^3

def test(N):
    tmp=N
    list=[]
    while tmp / 10.0 >0:
        s=tmp%10 #余数
        list.append(s)
        tmp=tmp//10 #取剩下的整商
    sum=0
    for item in list:
        sum+=item**len(list)
    if sum==N:     # or return sum ==N
        return True
    else:
        return False

N=123

def test2(N):
    strN=str(N)
    list=[]
    for item in strN: # list=[item for item in strN]
        list.append(item)
    sum=0
    for item in list:
        sum+=int(item)**len(list)
    return sum==N


def test2(N):
    strN=str(N)
    list=[]
    for item in strN: # list=[item for item in strN]
        list.append(item)
    sum=0
    for item in list:
        sum+=int(item)**len(list)
    return sum==N

res=test2(153)
print(res)

def test2(N): 
    l=list(str(N)) # not working
    sum=0
    for item in l:
        sum+=int(item)**len(l)
    return sum==N

res=test2(153)
print(res)







