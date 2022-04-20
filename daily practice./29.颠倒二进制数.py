#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:20:44 2022

@author: dantan
"""

def func(n):
    tip=0
    res=0
    while tip<32:
        tip+=1
        last=n&1
        res=(res<<1)+last
        n=n>>1
    return res

print(func(3))
