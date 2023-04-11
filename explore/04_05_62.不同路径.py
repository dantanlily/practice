#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:28:50 2023

@author: dantan
"""


# start loop from 1; initial values setting
def uniquePaths(m,n) -> int:
    dp=[[1 for i in range(n)] for j in range(m)]
    for i in range(1,m):
        for j in range(1,n): 
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[m-1][n-1])
    
    
