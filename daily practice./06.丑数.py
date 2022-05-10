#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:44:20 2022

@author: dantan
"""
#263 丑数 就是只包含质因数 2、3 和 5 的正整数。

# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ugly-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 丑数是指只包含质因数 2, 3, 5 的正整数。现在，输入一个正整数，判断其是否为丑数。


#
def test(N):
    if N<=0:
        return False
    for i in (2,3,5):
        while N%i==0:
            N=N/i
    if N==1:
        return True
    return False   # or directly using return n==1

test(12)

#
def test(N):
    if N<=0:
        return False
    if N==1:
        return True
    while N>=2:
        if N%2==0:
            N=N/2
            continue
        if N%3==0:
            N=N/3
            continue
        if N%5==0:
            N=N/5
            continue
        break   # important to have break there, for example 14
    if N==1:
        return True
    return False

test(12)

#264:给你一个整数 n ，请你找出并返回第 n 个 丑数 。丑数 就是只包含质因数 2、3 和/或 5 的正整数。

#method 1 time exceed
def test(N):
    if N<=0:
        return False
    for i in (2,3,5):
        while N%i==0:
            N=N/i
    if N==1:
        return True
    return False   # or directly using return n==1

def test2(N):
    num=1 # nth Ugly Number
    i=1 # Ugly Number value 
    while num<N:
        i+=1
        if test(i):
            num+=1
    return i

print(test2(600))
            
#method 2  
def test3(N):
    l=[1]
    p2=0 
    p3=0
    p5=0
    while len(l) < N:
        m=min(l[p2]*2,l[p3]*3,l[p5]*5)
        l.append(m)
        if l[p2]*2==m:
            p2+=1
        if l[p3]*3==m:
            p3+=1
        if l[p5]*5==m:
            p5+=1
    return l.pop()

print(test3(600))
            
        
       
            










































