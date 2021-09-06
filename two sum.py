#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:41:17 2021

@author: dantan
"""

from typing import List
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        m={}
        n=len(nums)
        for i in range(0,n):
            goal=target-nums[i]
            if (goal in m):
                return[m[goal],i]# read index
            m[nums[i]]=i # save/add new number position for later value search and index return
            # m[Key]=Value

s=Solution()
answer=s.twoSum([3,2,1,5],8)
print(answer)
