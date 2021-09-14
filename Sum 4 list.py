#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:00:38 2021

@author: dantan
"""

#https://leetcode.com/problems/4sum-ii/
#0 <= i, j, k, l < n
#nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m={}
        frequency=0
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]+nums2[j] not in m:
                    m[nums1[i]+nums2[j]]=0 # first occupy it with 0 to avoid error
                m[nums1[i]+nums2[j]]+=1
                
        for i in range(0,len(nums3)):
            for j in range(0,len(nums4)):
                target=-(nums3[i]+nums4[j])
                if target in m:
                    frequency+=m[target]
    
        return frequency


s=Solution()
answer=s.fourSumCount([-1,1],[1,-1],[-2,2],[2,-2])
print(answer)









