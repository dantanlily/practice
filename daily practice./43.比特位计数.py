#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:00:42 2022

@author: dantan
"""

# 338. 比特位计数
# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

 

# 示例 1：

# 输入：n = 2
# 输出：[0,1,1]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 示例 2：

# 输入：n = 5
# 输出：[0,1,1,2,1,2]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

from typing import List

# Quick way
class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            str=bin(i)
            c=str.count("1")
            l.append(c)
        return l

# slower
class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            n=i
            c=0  #每一个数n中二进制1的个数
            while n>0:
                c+=n&1
                n=n>>1
            l.append(c)
        return l
    
    
    
    
    
    
    