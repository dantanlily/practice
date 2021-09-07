#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:56:35 2021

@author: dantan
"""

# find majority element in a list
from typing import List

class Solution:
    def majorityElement(self,nums:List[int])->int:
        m={}
        for num in nums:
            m[num]=m.get(num,0)+1  # if has key as num, return value of m[num], else equal to 0
        for num in nums:
            if m[num]>len(nums)//2:
                return num

s=Solution()
answer=s.majorityElement([1,1,1,5])
print(answer)

