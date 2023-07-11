#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:37:29 2023

@author: dantan
"""

'''
70. 爬楼梯
提示
简单
3.1K
相关企业
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
 

提示：

1 <= n <= 45
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        #1 = 1
        #2 = 1 or 2 ->2 
        #3 = 1 1 1 ; 1 2; 2 1; ->3 
        #4 = 5 
        if n==1:
            return 1
        ways=[0]*(n+1)
        ways[0],ways[1]=1,1
        for i in range(2,n+1):
            ways[i]=ways[i-1]+ways[i-2]
        return ways[i]
