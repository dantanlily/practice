#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:10:06 2022

@author: dantan
"""

# 给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。

# 输入为 非空 字符串且只包含数字 1 和 0。

#  

# 示例 1:

# 输入: a = "11", b = "10"
# 输出: "101"
# 示例 2:

# 输入: a = "1010", b = "1011"
# 输出: "10101"

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/JFETK5
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

N = "11"
M = "10"

def test(N,M):# str
    i=0
    res=""
    tip=0#进位
    while i<len(N) or i<len(M) or tip==1:
        a=0
        b=0
        if i<len(N):
            a=int(N[len(N)-1-i])
        if i<len(M):
            b=int(M[len(M)-1-i])
        c=a+b+tip
        if c>=2:
            c=c-2
            tip=1
        else:
            tip=0
        res=str(c)+res#补到前一位
        i+=1
    return res

print(test(N,M))
print(test("010","111"))


def test2(N,M):
    return bin(int(N,2)+int(M,2))[2:] #变成十进制 #'0b101'







        