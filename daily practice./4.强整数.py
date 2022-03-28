#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:52:54 2022

@author: dantan
"""
# 970

#强整数有这样的定义，给定两个正整数x和y，如果某一整数等于xi + yj，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
#现在，输入x和y，给定一个上边界n，尝试编程找出小于等于n的所有强整数，通过列表的方式返回。

import math

def test(x,y,bounds):
    l=[]
    for i in range(0,bounds+1):
        if math.pow(x,i)>bounds:
            break
        for j in range(0,bounds+1):
            res=math.pow(x,i)+math.pow(y,j)
            if res<=bounds:
                if int(res) not in l: 
                    l.append(int(res))
            else:
                if x==1:
                    return l
                else:
                    break
    return l

print(test(2,3,10))


x,y,bound=2,3,10


#优化上限 元组+栈结构 用元组存储x,y
def test2(x,y,bounds):
    l=[]
    stack=[(0,0)]
    while len(stack)>0:
        tmp=stack.pop() #(0,0)
        res=math.pow(x,tmp[0])+math.pow(y,tmp[1])
        if res<=bounds:
            if int(res) not in l:
                l.append(int(res))
            if x>1:
                stack.append((tmp[0]+1,tmp[1]))
            if y>1:
                stack.append((tmp[0],tmp[1]+1))
    return l # or return set(l) if no 'if int(res) not in l:'

test2(2,3,10)
#[2, 4, 10, 5, 7, 3, 9]

x,y,bound=2,3,10

# better, time limit exceed
def test2(x,y,bounds):
    l=[]
    stack=[(0,0)]
    while len(stack)>0:
        tmp=stack.pop() #(0,0)
        res=math.pow(x,tmp[0])+math.pow(y,tmp[1])
        if res<=bounds:
            l.append(int(res))
            if x>1:
                stack.append((tmp[0]+1,tmp[1]))
            if y>1:
                stack.append((tmp[0],tmp[1]+1))
    return set(l) # or return set(l) if no 'if int(res) not in l:'

test2(2,2,400000)  

def test3(x,y,bounds):
    l=[]
    stack=[(0,0)]
    while len(stack)>0:
        tmp=stack.pop() #(0,0)
        res=x**tmp[0]+y**tmp[1]
        if res<=bounds:
            l.append(int(res))
            if x>1:
                stack.append((tmp[0]+1,tmp[1]))
            if y>1:
                stack.append((tmp[0],tmp[1]+1))
    return set(l) # or return set(l) if no 'if int(res) not in l:'

test3(2,2,400000)  


test2(2,3,10)

# accepted
def powerfulIntegers(x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        dpx = list()
        dpy = list()
        res = list()
        if x != 1:
            t = 0
            while( x **t < bound):
                dpx.append(x **t)
                t += 1
        else:
            dpx = [1]
        if y != 1:

            t = 0
            while(y **t < bound):
                dpy.append(y ** t)
                t += 1
        else:
            dpy = [1]

        for i, x in enumerate(dpx):
            for j, k in enumerate(dpy):
                t = x + k
                if t <= bound:
                    res.append(t)
        return list(set(res))

powerfulIntegers(2,2,400000)  
                