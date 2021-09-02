#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:37:47 2021

@author: dantan
"""

from typing import List

class Solution:
    def missingNumber(self,nums: List[int]):
        currentSum=sum(nums)
        n=len(nums)
        intendedSum=n*(n+1)/2
        
        return int(intendedSum-currentSum)
    
s=Solution()
answer=s.missingNumber([0,3,1,2,5])
print(answer)

#Also consider sort, -1; Also Hashmaps, TRUE