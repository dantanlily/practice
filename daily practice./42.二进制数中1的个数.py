#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 21:08:18 2022

@author: dantan
"""

# 191. 位1的个数
# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

# 提示：

# 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
 
# 示例 1：

# 输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
# 示例 2：

# 输入：00000000000000000000000010000000
# 输出：1
# 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
# 示例 3：

# 输入：11111111111111111111111111111101
# 输出：31
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
 
# 提示：

# 输入必须是长度为 32 的 二进制串 。
 
# 进阶：

# 如果多次调用这个函数，你将如何优化你的算法？

# def countPrimes(n):
#     # 0 and 1 is not primes
#     l=[1]*n
#     for i in range(2,n):
#         if l[i]==1:
#             for j in range(2*i,n,i):
#                     l[j]=0
#         return sum(l)-2 if n>1 else 0
    


# Exceed 99.67% percent
class Solution:
    def hammingWeight(self, n: int) -> int:
        str=bin(n)
        c=str.count("1")
        return c
    
    
#Exceed 76.2% percent

class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n>0:
           c+=n&1
           n=n>>1
        return c



# another case L and R 
import math
    
def isPrime(n):
    if n<2:
        return False
    i=2
    while i<=int(math.sqrt(n)):
        if n%n==0:
            return False
        i+=1
    return True

def func(L,R):
    res=0
    for i in range(L,R+1):
        n=i
        c=0
        while n>0:
            c+=n&1
            n=n>>1
        if isPrime(c):
            res+=1
    return res


print(func(2,7))

# more efficient

def func2(L,R):
    res=0
    for i in range(L,R+1):
        str=bin(i)
        c=str.count("1")
        if isPrime(c):
            res+=1
    return res

print(func2(2,7))



