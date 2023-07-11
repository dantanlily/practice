#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:27:03 2023

@author: dantan
"""

'''
343. 整数拆分
提示
中等
1.2K
相关企业
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。

 

示例 1:

输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
 

提示:

2 <= n <= 58
'''

n=10
def integerBreak(n):
    '''
    dp[i] 对i拆分得到最大的乘积dp[i]
    两个数： 不用loop j*(i-j)
    三个数以上：j*dp[i-j]
    '''
    dp=[0]*(n+1)
    dp[0],dp[1],dp[2]=0,0,1
    for i in range(3,n+1):
        for j in range(1,int(i/2)+1): 
            dp[i]=max(dp[i],max(j*(i-j),j*dp[i-j]))
            #print(i,dp[i])
    return dp[n]
        
        
  

























