#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:44:45 2022

@author: dantan
"""

## Two Number Sum

#### Problem Statement

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the
target sum, the function should return them in an array, in sorted order. If no two numbers sum up to the target sum, the function should return an empty array.
Assume that there will be at most one pair of numbers summing up to the target sum.

`Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]`

# In[]
# o(n^2) time | o(1) space
def twonumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstNum=array[i]
        for j in range(i+1,len(array)):
            secondNum=array[j]
            if firstNum+secondNum==targetSum:
                return [firstNum,secondNum]
    return []

# In[]
# o(n) time | o(n) space
def twonumberSum(array,targetSum):
    nums={}
    for num in array:
        if targetSum-num in nums: # targetSum-num: potentialMatch
            return [targetSum-num,num]
        else:
            nums[num]=True
    return []

# In[]
# o(nlog(n)) time | o(1) space
def twonumberSum(array,targetSum):
    array.sort()
    left=0
    right=len(array)-1
    while left < right:
        currentSum=array[left]+array[right]
        if currentSum==targetSum:
            return [array[left],array[right]]
        elif currentSum<targetSum:
            left+=1
        elif currentSum>targetSum:
            right-=1
    return []
        
# In[]

twonumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)






