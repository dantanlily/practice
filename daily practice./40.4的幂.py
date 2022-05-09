#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:25:03 2022

@author: dantan
"""

# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

#  

# 示例 1：

# 输入：n = 16
# 输出：true
# 示例 2：

# 输入：n = 5
# 输出：false
# 示例 3：

# 输入：n = 1
# 输出：true
#  

# 提示：

# -231 <= n <= 231 - 1
#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/power-of-four
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def func(n):
    s=4
    while s<n:
        s*=4
    if n==1 or s==n:
        return True
    return False

func(4)


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        s=4
        while s<n:
            s*=4
        if n==1 or s==n:
            return True
        return False










