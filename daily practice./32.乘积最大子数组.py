#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:47:01 2022

@author: dantan
"""
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

# 测试用例的答案是一个 32-位 整数。

# 子数组 是数组的连续子序列。

#  

# 示例 1:

# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:

# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-product-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #三种情况 
        # current 5 next 10
        # current -5 next -10
        # current -5, next 10000  
        max_=min_=res=nums[0]
        for i in range(1,len(nums)):
            temp=max_
            max_=max(max(max_*nums[i],min_*nums[i]),nums[i])
            min_=min(min(min_*nums[i],temp*nums[i]),nums[i])
            res=max(max_,res)
        return res







