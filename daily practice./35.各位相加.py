#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 18:49:08 2022

@author: dantan
"""
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

#  

# 示例 1:

# 输入: num = 38
# 输出: 2 
# 解释: 各位相加的过程为：
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# 由于 2 是一位数，所以返回 2。
# 示例 1:

# 输入: num = 0
# 输出: 0

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-digits
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


#abc=100*a+10*b+c= 99a+9b+ a+b+c

def func(n):
    if n==0:
        return 0
    res=n%9
    if res==0:
        return 9
    else:
        return res

print(func(9183))


def func(n):
    res=n
    while res>9:
        temp=res
        res=0
        t=list(str(temp))
        for i in t:
            res+=int(i) #继续转化为整数
    return res


def func(n):
    l=list(str(n))
    res=0
    for i in l:
        res+=int(i)
    while res>9:
        temp=res
        res=0
        t=list(str(temp))
        for i in t:
            res+=int(i)
    return res








print(func(12388))





