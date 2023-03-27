#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:53:21 2023

@author: dantan
"""

# 
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
def fib(n):
    if n<2:
        return n
    a,b,c=0,1,0
    for i in range(1,n):
        c=a+b
        a,b=b,c
    return c

# In[] 
# 创建 初始化 遍历 返回
def fib(n):
    if n==0:
        return 0
    # 创建 dp table 
    dp=[0]*(n+1)
    
    #初始化
    dp[0],dp[1]=0,1
    
    #遍历顺序；由前向后 因为后面要用到前面的状态
    for i in range(2,n+1):
        #确定递归公式/状态转移公式
        dp[i]=dp[i-1]+dp[i-2]
    #返回答案
    return dp[n]

# In[]

# 递归实现
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
    
    
    
    
    
    
    
    
    
    
    
    
