#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:39:42 2023

@author: dantan
"""

'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 
提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
'''

nums = [2,7,11,15] 
target = 9

nums=[3,3]
target=6


# nums[3,3] 先判断第二个3 在不在第一个dict中 先判断 后储存 这样不会造成override index情况
def twoSum(nums,target):
    dic={}
    for i in range(len(nums)):
        if target-nums[i] in dic:
            return i,dic[target-nums[i]]
        dic[nums[i]]=i
        
# In[]使用集合

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #创建一个集合来存储我们目前看到的数字
        seen = set()             
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
