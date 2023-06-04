#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 23:04:01 2023

@author: dantan
"""
'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

'''

nums = [-1,0,3,5,9,12]
target = 9
#[] 以mid为起始点 看大小 调整左右边界 左闭又闭 
# right不用每次只前进一步 直接用middle定义边界 
def search(nums):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right-=1
        else:
            left+=1
    return -1

'''
时间复杂度：O(log n)
空间复杂度：O(1)
'''
# 左闭右闭 

def search_1(nums):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1



#[]以mid为起始点 看大小 调整左右边界 左闭右开[) 右边边界取不到 最快 
def search_2(nums):
    left=0
    right=len(nums)
    while left<right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right=mid
        else:
            left=mid+1
    return -1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
    
    
