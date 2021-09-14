#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:44:28 2021

@author: dantan
"""

#https://leetcode.com/problems/triangle/

#Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
#Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# # triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

# #dp=[[0]*i for i in range(1,len(triangle)+1)]

# dp = triangle[:]
# for i in range(1, len(dp)):
#     dp[i][0] += dp[i - 1][0]
#     dp[i][-1] += dp[i - 1][-1]
#     for j in range(1, len(dp[i]) - 1):
#         dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j])
    

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1,len(triangle)):
            triangle[i][0]+=triangle[i-1][0]
            triangle[i][-1]+=triangle[i-1][-1]
            for j in range(1,i):# len(triangle[i]-1)
                triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])