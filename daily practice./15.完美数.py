#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:41:55 2022

@author: dantan
"""
# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。

# 给定一个 整数 n， 如果是完美数，返回 true；否则返回 false。

#  

# 示例 1：

# 输入：num = 28
# 输出：true
# 解释：28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, 和 14 是 28 的所有正因子。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/perfect-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import math
def func(n):
    if n<=0:
        return False
    res=0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i==0: #成对因素 
            res+=i
            if i*i!=n:
                res+=n/i
    if res==n*2: #因为1 把原本数n也会加上去 * 2
        return True
    return False
    