#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:29:11 2022

@author: dantan
"""

# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 例如，121 是回文，而 123 不是。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def test(N):
    list1=list(str(N))
    list2=list(str(N))
    list2.reverse()
    return list1==list2

print(test(11211))

def test(N):
    return str(N)==str(N)[::-1]

print(test(11211))


# 回文素数 只能被1和本身整除
# time limit  exceed
def numCheck1(N):
    return str(N)==str(N)[::-1]

import math
def numCheck2(N):
    if N==1:
        return False
    for i in range(2,int(math.sqrt(N)+1)):
        if N%i==0:
            return False
    return True

def test(N):
    while True:
        if numCheck1(N):
            if numCheck2(N):
                return N
        N=N+1

print(test(200000000)) # time exceed
print(test(8)) # time exceed

#优化
# 除11以外的偶数位回文数，都能被11整除。
# 除了2和3外，其他所有的素数对6去取余一定等于5或者等于1。
# 
import math
def numCheck1(N):
    return str(N)==str(N)[::-1]

def numCheck2(N):
    if N==1:
        return False
    for i in range(2,int(math.sqrt(N)+1)):
        if N%i==0:
            return False
    return True

def test(N):
    while True:
        string=str(N)
        #除11以外的偶数位回文数，都能被11整除。
        if N >11 and len(string) % 2==0:
            new_string=""
            for i in range(0,len(string)): # move from 1000 to 10001
                new_string=new_string+"0"
            new_string="1"+new_string
            N=int(new_string)+1
            continue # 
        #除了2和3外，其他所有的素数对6去取余一定等于5或者等于1。
        temp=0
        if N>3: 
            temp = N%6 #余数
        if temp>0 and temp!=1 and temp!=5:  #sometimes having some problems
            continue
        if numCheck1(N):
            if numCheck2(N): 
                return N
        #N=N+1
        # 调整步长可以进一步加快速度 不直接用N+1
        if temp==1:
            N=N+4
        elif temp==5:
            N=N+2
        else:
            N=N+1


print(test(20000000)) # time exceed

























