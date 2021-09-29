#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:58:12 2021

@author: dantan
"""

# Bruteforce

#Time complexity : O(Nk), where N is number of elements in the array.

#Space complexity : O(N−k+1) for an output array.

from typing import List
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n=len(nums)
        if n*k==0:
            return []
        # n-k +1 sliding window
        return [max (nums[i:i+k]) for i in range(n-k+1)]
    
s=Solution()
s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)

#[3, 3, 5, 5, 6, 7]


# 
def maxSlidingWindow1(nums,k):
    if not nums: return []
    window,res=[],[]
    for i,x in enumerate(nums):
        # window size always is k, save index number
        if i>=k and window[0]<=i-k:
            window.pop(0) # remove the existed first index
        while window and nums[window[-1]]<=x: 
            window.pop()
        window.append(i)
        if i>=k-1:
            res.append(nums[window[0]])
    return res

maxSlidingWindow1([1,3,-1,-3,5,3,6,7],3)          
            

