#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:23:53 2023

@author: dantan
"""

n=3

def numTrees(n):
    dp=[0]*(n+1)
    dp[0]=1
    # dp[1]=dp[0]*dp[0]
    # dp[2]=dp[1]*dp[0]+dp[1]*dp[0]
    # #左节点 右节点
    # dp[3]=dp[2]*dp[0]+dp[1]*dp[1]+dp[0]*dp[2]
    # dp[i]+=dp[j-1]*dp[i-j]
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i]+=dp[j-1]*dp[i-j]
    print(dp[n])
            #print(i,j)
            #print('dp',j-1,i-j)

# In[]
class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        # dp[1]=dp[0]*dp[0]
        # dp[2]=dp[1]*dp[0]+dp[1]*dp[0]
        # #左节点 右节点
        # dp[3]=dp[2]*dp[0]+dp[1]*dp[1]+dp[0]*dp[2]
        # dp[i]+=dp[j-1]*dp[i-j]
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[n]
