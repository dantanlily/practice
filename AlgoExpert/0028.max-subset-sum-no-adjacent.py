#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:52:46 2022

@author: dantan
"""
# Write a function that takes in an array of positive integers and returns an integer representing the maximum sum of non-adjacent elements in the array. If a sum
# cannot be generated, the function should return 0.

# Sample input: [75, 105, 120, 75, 90, 135]
# Sample output: 330 (75, 120, 135)

# In[] o(n)time o(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array)==1:
        return array[0]
    # max1, max(max1,num2),max1+num3/max2;
    maxSums=array[:]
    maxSums[1]=max(array[0],array[1])
    for i in range(2,len(maxSums)):
        maxSums[i]=max(maxSums[i-2]+array[i],maxSums[i-1])
    return maxSums[-1]

maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])

# In[] o(n)time o(1) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array)==1:
        return array[0]
    # max1, max(max1,num2),max1+num3/max2;
    second=array[0]
    first=max(array[0],array[1])
    for i in range(2,len(array)):
        current=max(first+array[i],second)
        second=first
        first=current
    return first

maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])





