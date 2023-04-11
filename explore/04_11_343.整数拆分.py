#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:43:27 2023

@author: dantan
"""

n=10
# dp[i] i 拆分的最大积为dp[i]

def integerBreak(n):
    if n==2:
        return 1  
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=0
    dp[2]=1
    # think about dp[n] meaning, then can set up dp to n+1 length
    for i in range(3,n+1):
        for j in range(1,int(n/2)+1):
            dp[i]=max(j*(i-j),j*dp[i-j],dp[i])# calculate from small to big, every steps
    print(dp[n])
    
# In[]
class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1  
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=0
        dp[2]=1
        # think about dp[n] meaning, then can set up dp to n+1 length
        for i in range(3,n+1):
            for j in range(1,int(n/2)+1):
                dp[i]=max(j*(i-j),j*dp[i-j],dp[i])# calculate from small to big, every steps
        return dp[n]
    