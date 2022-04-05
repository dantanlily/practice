#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:34:27 2022

@author: dantan
"""

# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

# 请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。

#  

# 示例 1:

# 输入: num = "69"
# 输出: true
# 示例 2:

# 输入: num = "88"
# 输出: true
# 示例 3:

# 输入: num = "962"
# 输出: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/strobogrammatic-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def func(n):
    dic={"0":"0","1":"1","2":"-1","3":"-1","4":"-1","5":"-1","6":"9","7":"-1","8":"8","9":"6"}
    l=[]
    for c in n:
        if dic[c] =="-1":
            return False
        l.insert(0,dic[c])#逆序 新的映射对称数c在0位置插入
    return n=="".join(l) #['6','9'] to '69'

print(func("169"))
print(func("69"))

# for c in "69":
#     print(c) # 6 9

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        