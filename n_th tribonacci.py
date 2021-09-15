#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:01:51 2021

@author: dantan
"""

#https://leetcode.com/problems/n-th-tribonacci-number/

#The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

from typing import List

class Solution:
    def tribonacci(self, n: int) -> int:
        while n!=0 and n!=1 and n!=2:
            tri_list=[0]*n
            tri_list[1]=1
            tri_list[2]=1
            for i in range(0,n-3):
                tri_list[i+3]=tri_list[i+2]+tri_list[i+1]+tri_list[i]
            return tri_list[-1]+tri_list[-2]+tri_list[-3]
        if n==0:
            return n
        return 1

s=Solution()
s.tribonacci(1)

# note that n can be equal to 0,1,2, unique cases need to be added