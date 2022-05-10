#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:17:34 2022

@author: dantan
"""

#完全平方数有这样的特性：如果一个正整数a是某一个整数b的平方，那么这个正整数a叫做完全平方数，零也可称为完全平方数。那么：
#给定正整数n，找到若干个完全平方数使得它们的和等于n。你需要确定组成和的完全平方数的最少的个数。例如：对于正整数13，其可以拆解为13 = 4 + 9，则最少个数为2。对于正整数12，其可以拆解为 12 = 4 + 4 + 4，则最少个数为3。

#四平方数和定理又称拉格朗日四平方数和定理，由拉格朗日最终解决，四平方数和定理可以证明：任何正整数均可表示为四个整数的平方和(其中允许有整数为0)。 
#如果一个数n只能使用4个非零的完全平方数的和表示，则这个数n一定满足4^a(8b+7) 

# different scenarios; 4 number, 1 number, 2 number, 
def test(n):
    num=n
    while num%4 ==0:
        num=num/4
    if num%8 ==7:
        return 4
    for i in range(1,n+1):
        if i*i ==n:
            return 1
    for i in range(1,n+1):
        for j in range(1,n+1): # range(1,n-i*i+1)
            if i*i+j*j==n:
                return 2
    return 3

print(test(7000))


import math

def test2(n):
    num=n
    while num%4 ==0:
        num=num/4
    if num%8 ==7:
        return 4
    if math.pow(int(math.sqrt(n)),2)==n:
        return 1
    max_=int(math.sqrt(n))+1
    for i in range(1,max_):
        tmp=n-i*i
        if math.pow(int(math.sqrt(tmp)),2)==tmp:
            return 2
    return 3

print(test2(7000))








