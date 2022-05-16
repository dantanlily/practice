#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:51:39 2022

@author: dantan
"""
# 整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

# 示例1:

#  输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
#  输出：2
# 示例2:

#  输入：A = 1，B = 2
#  输出：2
# 提示:

# A，B范围在[-2147483648, 2147483647]之间


# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/convert-integer-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def func(A,B):
    res=A^B #不同位为1
    c=bin(res).count("1")
    return c

print(func(3,4))

#not work for func(-1,1); output should be 31


# 1   0000 0000 0000 0000 0000 0000 0000 0001
# -1  1111 1111 1111 1111 1111 1111 1111 1111 #相反数取反码再+1

print(bin(-1)) #-0b1

print(bin(-1 & 0xffffffff)) #0b11111111111111111111111111111111


# exceed 100% 
def func(A,B):
    A=A& 0xffffffff # 32位1
    B=B& 0xffffffff
    res=A^B
    c=bin(res).count("1")
    return c
print(func(-1,1))






