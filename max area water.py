#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:33:15 2021

@author: dantan
"""
from typing import List 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while (left<right):
            max_area=max(max_area,min(height[right],height[left])*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
    
#create a instance
s=Solution()
answer=s.maxArea([1,8,6,2,5,4,8,3,7])
print(answer)
# 2,1,4,0,0