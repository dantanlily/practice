#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:55:47 2022

@author: dantan
"""
# 69. x 的平方根 
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

 

# 示例 1：

# 输入：x = 4
# 输出：2
# 示例 2：

# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

import math

def func(n):
    l=0
    r=n
    while l<r:
        s=int((l+r)/2)
        if s*s==n:
            return s
        elif s*s<n:
            l=s+1
        else:
            r=s-1
    if l*l>n:
        return int(l-1)
    else:
        return int(l)
    
print(math.sqrt(300))

print(func(300))


#注意边界 
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            s = mid ** 2
            if s == x:
                return mid
            elif s < x:
                left = mid + 1
            elif s > x:
                right = mid - 1
        return left - 1

def mySqrt(x):
    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        s = mid ** 2
        if s == x:
            return mid
        elif s < x:
            left = mid + 1
        elif s > x:
            right = mid - 1
    return left - 1

print(math.sqrt(300))

print(func(300))





