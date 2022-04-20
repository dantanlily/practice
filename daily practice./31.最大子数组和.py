#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:18:09 2022

@author: dantan
"""
# 53. 最大子数组和
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组 是数组中的一个连续部分。

 

# 示例 1：

# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：

# 输入：nums = [1]
# 输出：1
# 示例 3：

# 输入：nums = [5,4,-1,7,8]
# 输出：23

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #连续子数组
        max_sub=0
        ans=-99999999
        for i in range(len(nums)):
            if max_sub<0:
                max_sub=0
            max_sub+=nums[i]
            if (ans<max_sub):
                ans=max_sub
        if ans<0:
            return max(nums)
        return ans

#贪心算法 若当前指针所指元素之前的和小于0，则丢弃当前元素之前的数列
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:return -2147483648
        
        cur_sum=max_sum=nums[0]
        for i in range(1,len(nums)):
            cur_sum=max(nums[i],cur_sum+nums[i])
            max_sum=max(cur_sum,max_sum)
        return max_sum

#动态规划 若前一个元素大于0，则将其加到当前元素上
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
        return max(nums)
    
    
    
    
    
    
    


