#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:00:01 2021

@author: dantan
"""
from typing import List

# nums=[1,3,1,3,100]
# nums=[2,3,2]

# if len(nums)==0:
#     print(nums[0])


# dp=[0]*len(nums)    
# dp[0]=nums[0]
# dp[1]=max(nums[0],nums[1])

# for i in range(2, len(nums)): 
#     dp[i]=max(dp[i-2]+nums[i],dp[i-1])
# print(dp[-1])

# nums[1:]
# nums[:-1]

# nums=[0,0]
# print(max(nums[0],nums[1]))

#213. House Robber II
#https://leetcode.com/problems/house-robber-ii/
class Solution:
    
    def rob(self, nums: List[int]) -> int:
         if len(nums)==1:
            return nums[0]
         if len(nums)==2:
            return max(nums[0],nums[1])
         return max(self.rob2(nums[1:]),self.rob2(nums[:-1]))
        
    def rob2(self, nums: List[int]) -> int:
        
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return(dp[-1])
    
#   
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.rob2(nums[1:]), self.rob2(nums[:-1]))
    
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return 0
        if not nums:
            return 0
        dp = [0 for _ in nums]
        dp[0] = nums[0] 
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(dp[0], nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

#198. House Robber
#https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        else:
            dp=[0]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(dp[i-2]+nums[i],dp[i-1])
            return dp[-1]
        
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return 0
        if not nums:
            return 0
        dp = [0 for _ in nums]
        dp[0] = nums[0] 
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(dp[0], nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]