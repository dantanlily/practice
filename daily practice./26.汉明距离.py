#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 22:05:50 2022

@author: dantan
"""
# 两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

# 给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

 

# 示例 1：

# 输入：x = 1, y = 4
# 输出：2
# 解释：
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 上面的箭头指出了对应二进制位不同的位置。
# 示例 2：

# 输入：x = 3, y = 1
# 输出：1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/hamming-distance
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

m=10
n=15
def func(m,n):
    res=m^n #筛选所有不同位置 异或为1
    c=0 
    #判断二进制数中有多少个1
    while res>0:
        c+=res&1 #00001 任何一个数和1 与 either 1 or 0
        res=res>>1
    return c

print(func(10,15))

#   m=1010 =10
#   n=1111 =15
# res=0101 = 5 
# &1 =0001
# c  =0001

# res>>1
# res=010
# =   001
# c=0

# res
# 11011
# 1101 
    
    












