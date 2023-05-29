#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 23:46:14 2023

@author: dantan
"""

'''
977. 有序数组的平方
1130
807
第 120 场周赛
Q1
相关企业
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

 

示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
 

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序
 

进阶：

请你设计时间复杂度为 O(n) 的算法解决本问题
'''

nums = [-4,-1,0,3,10]
#输出：[0,1,9,16,100]

nums = [-7,-3,2,3,11]

# 原list已经排好序 最大的应该在两边 需要考虑两边数值 从两边到中间 

def sortedSquares(nums):
    left=0
    right=len(nums)-1
    nums2=[0]*len(nums)
    index=len(nums)-1
    while left<=right: 
        if nums[left]**2<=nums[right]**2:
            nums2[index]=nums[right]**2
            right-=1
            index-=1
            
        else:
            nums2[index]=nums[left]**2
            left+=1
            index-=1
    return nums2
    #print(nums2)

#可以把index提出来 放到和if else并列地方
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        nums2=[0]*len(nums)
        index=len(nums)-1
        while left<=right: 
            if nums[left]**2<=nums[right]**2:
                nums2[index]=nums[right]**2
                right-=1
            else:
                nums2[index]=nums[left]**2
                left+=1
            index-=1
        return nums2           
# In[]
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i,j,k = 0,n - 1,n - 1
        ans = [-1] * n
        while i <= j:
            lm = nums[i] ** 2
            rm = nums[j] ** 2
            if lm > rm:
                ans[k] = lm
                i += 1
            else:
                ans[k] = rm
                j -= 1
            k -= 1
        return ans
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    





