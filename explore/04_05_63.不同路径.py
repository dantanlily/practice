#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:00:36 2023

@author: dantan
"""

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# note cannot use same array for dp and obtacleGrid
# set up dp specifically
def uniquePathsWithObstacles(obstacleGrid):
    m=len(obstacleGrid) # row
    n=len(obstacleGrid[0]) # column
    dp=[[0 for _ in range(n)] for _ in range(m)] # first create columns, then loop rows
    if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
        print(0)
    # initial values set up
    for i in range(m):
        if obstacleGrid[i][0]==1: 
            break
        else: 
            dp[i][0]=1
    for j in range(0,n):
        if obstacleGrid[0][j]==1: 
            break
        else: 
            dp[0][j]=1
    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j]!=1:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                #print(i,j,dp[i][j])
    print(dp[m-1][n-1])
    
# In[] submit
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid) # row
        n=len(obstacleGrid[0]) # column
        dp=[[0 for _ in range(n)] for _ in range(m)] # first create columns, then loop rows
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        # initial values set up
        for i in range(m):
            if obstacleGrid[i][0]==1: 
                break
            else: 
                dp[i][0]=1
        for j in range(0,n):
            if obstacleGrid[0][j]==1: 
                break
            else: 
                dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                    #print(i,j,dp[i][j])
        return dp[m-1][n-1]
    
     