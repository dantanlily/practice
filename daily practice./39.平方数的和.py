#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:15:41 2022

@author: dantan
"""

# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

#  

# 示例 1：

# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
# 示例 2：

# 输入：c = 3
# 输出：false
#  

# 提示：

# 0 <= c <= 231 - 1

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sum-of-square-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import math

def func(n):
    l=0
    r=int(math.sqrt(n))
    while l<=r:
        res=l*l+r*r
        if res<n:
            l+=1
        elif res>n:
            r-=1
        else:
            print(l)
            print(r)
        return True
    return False

print(func(5))


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(math.sqrt(c))
        while l<=r:
            res=l*l+r*r
            if res<c:
                l+=1
            elif res>c:
                r-=1
            else:
                #print(l)
                #print(r)
                return True
        return False