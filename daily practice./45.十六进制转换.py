#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 01:15:40 2022

@author: dantan
"""
# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

# 注意:

# 十六进制中所有字母(a-f)都必须是小写。
# 十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
# 给定的数确保在32位有符号整数范围内。
# 不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
# 示例 1：

# 输入:
# 26

# 输出:
# "1a"
# 示例 2：

# 输入:
# -1

# 输出:
# "ffffffff"

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/convert-a-number-to-hexadecimal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def func(n):
    n=n&0xffffffff #纯1 要内存中原始的数据 注意f个数 -1保持一致
    #列表映射2进制和16进制关系
    l=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    res=""
    while n>0:
        temp=n&0xf # 000001111 #把原数的四位取出来
        res=l[temp] + res
        n=n>>4
    if res=="":
        res="0"
    return res
    
print(func(-1))
print(func(100))
print(func(10))







