#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:16:48 2023

@author: dantan
"""

'''
416. 分割等和子集
中等
1.8K
相关企业
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
'''
nums = [1,5,11,5]
def canPartition(nums):
    #注意处理奇数
    if sum(nums)%2==1:
        return False
    target=sum(nums)//2
    dp=[0]*100000 # 200*100
    for num in nums:
        for j in range(target,num-1,-1):
            dp[j]=max(dp[j],dp[j-num]+num)
    if dp[target]==target:
        print('True') # return True
    else:
        print('False') # return False
        
# In[] example
from typing import List 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = 0
    
        # dp[i]中的i表示背包内总和
        # 题目中说：每个数组中的元素不会超过 100，数组的大小不会超过 200
        # 总和不会大于20000，背包最大只需要其中一半，所以10001大小就可以了
        dp = [0] * 10001
        for num in nums:
            _sum += num
        # 也可以使用内置函数一步求和
        # _sum = sum(nums)
        if _sum % 2 == 1:
            return False
        target = _sum // 2
    
        # 开始 0-1背包
        for num in nums:
            for j in range(target, num - 1, -1):  # 每一个元素一定是不可重复放入，所以从大到小遍历
                dp[j] = max(dp[j], dp[j - num] + num)
    
        # 集合中的元素正好可以凑成总和target
        if dp[target] == target:
            return True
        return False

    



















