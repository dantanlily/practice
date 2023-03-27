#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:54:19 2023

@author: dantan
"""
cost = [1,100,1,1,1,100,1,1,100,1]
cost = [10,15,20]
# initial values and boundries are important
def minCostClimbingStairs(cost):
    n=len(cost)
    # cannot equal to 2; if [1,100], min=1
    if n<2:
        return 0
    dp=[0]*(n+1)
    #注意边界 可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
    #往上爬了之后 才花费本台阶的体力值
    dp[0]=0
    dp[1]=0
    for i in range(2,n+1):
        dp[i]=min((dp[i-1]+cost[i-1]),dp[i-2]+cost[i-2]) 
    return dp[n]
    
minCostClimbingStairs(cost)

