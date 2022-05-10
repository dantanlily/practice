#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:46:07 2022

@author: dantan
"""
# 204. 计数质数
# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。

 

# 示例 1：

# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 示例 2：

# 输入：n = 0
# 输出：0
# 示例 3：

# 输入：n = 1
# 输出：0
 

# 提示：

# 0 <= n <= 5 * 106


# quick way

class Solution:
    def countPrimes(self, n: int) -> int:
        # 0 and 1 is not primes
        l=[1]*n
        for i in range(2,n):
            if l[i]==1:
                for j in range(2*i,n,i):
                    l[j]=0
        return sum(l)-2 if n>1 else 0

#

import math

def isPrime(n):
    i=2
    while i<=int(math.sqrt(n)):
        if n%i==0:
            return False
        i+=1
    if n>=2:
        return True
    return False
        

def func(n):
    c=0
    for i in range(0,n):
        if i<2:
            continue
        if isPrime(i):
            c+=1
    return c

print(func(1200))












