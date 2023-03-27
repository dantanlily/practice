#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:58:18 2023

@author: dantan
"""


# dp[n] 需要多少方法到楼顶
# n=1  1 
# n=2  1+1; 2; 2种
# n=3  2种+1种

# In[] 空间复杂度O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    
# In[] 空间复杂度 O(1)
def climbStairs(self, n: int) -> int:
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        tmp=dp[1]+dp[2]
        dp[1]=dp[2]
        dp[2]=tmp
        
    return dp[2]

# In[] to be updated; if can take step 1, 2, ....m at one time, how many...? in total









# In[]
a=0
b=1
print(a or b)

def rec(a,b):
    if a==0:
        return b
    else:
        return rec(a-1,a+b)
print(rec(8,12))






