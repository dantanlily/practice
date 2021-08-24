#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:48:44 2021

@author: dantan
"""

#  an increasing subsequence followed by a deacreasing subsequence

from typing import List 

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:
            return False
        i=1
        
        while (i<len(A) and A[i]>A[i-1]):
            i+=1
        if (i==1 or i==len(A)):
            return False
        
        while (i<len(A) and A[i]<A[i-1]):
            i+=1
        
        return i==len(A)

#create a instance
s=Solution()
answer=s.validMountainArray([1,2,5,4,3])
print(answer)
# 2,1,4,0,0