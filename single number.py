#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:55:49 2021

@author: dantan
"""
# Given a non-empty array of integers, every element appears twice except for one, find it

class Solution(object):
    def singleNumber(self,nums):
        
        # type nums: List[int]
        # rtype: int
        
        return 2*sum(set(nums))-sum(nums)

s=Solution()
answer=s.singleNumber([3,3,2,2,1])
print(answer)