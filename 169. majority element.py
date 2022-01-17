#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:38:40 2022

@author: dantan
"""

# 169 Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 

from typing import List

#1 sort O(NlogN) fatest in actual implementation
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[int(len(nums) / 2)]



nums=[1,3,3,2,3]

# 2. hash
def majorityElement(nums):
    dict1={}
    for i in nums:
        if i not in dict1: # first value appear, set a value to avoid error
            dict1[i]=0
        dict1[i]+=1 # first time nums appear assigns 0 dict1.get(i,0)
    max_value=max(dict1.values()) # dict.items(); dict.keys()
    return [k for k,v in dict1.items() if v==max_value][0]

majorityElement(nums)


# 3. divide and conquer O(NlogN)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(l, r) :
            if l == r : return nums[l]
            m = l + (r - l) // 2  
            leftMajor = helper(l, m)
            rightMajor = helper(m + 1, r)
            if leftMajor == rightMajor : return leftMajor
            leftCount = sum(1 for i in range(l, r + 1) if nums[i] == leftMajor)
            rightCount = sum(1 for i in range(l, r + 1) if nums[i] == rightMajor)
            return leftMajor if leftCount > rightCount else rightMajor

        return helper(0, len(nums) - 1)

s=Solution()
s.majorityElement(nums)

# l=0
# r=len(nums)-1 = 4
# m=2
















