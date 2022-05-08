#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:11:09 2022

@author: dantan
"""
# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

#  

# 示例:

# 输入: a = 1, b = 1
# 输出: 2

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 要解决本题其实并不难，重要的是我们要了解二进制运算的一个有趣的特点，对两个正整数进行异或运算，得到的结果实际上就是两数相加后所有不需要进位的位，例如二进制数1101与二进制数1000进行异或，将得到结果0101。
# 同样对两个数进行与运算得到的结果实际上是需要进位的位，例如二进制数1101与二进制数1000进行按位与运算，将得到结果1000，这个结果中实际上记录了在实际相加运算时所有需要向左进1的位，我们只需要统一做一次左移运算即可。
# 重复上面的两种操作，直到不再有进位的位出现，则表明我们得到了最终的运算结果。 

1100
1001 ^异或运算 异或运算后为1的为不需要进位的位；相同为0 不同为1 

0101 未进位

1000 &需要进位


def func(a,b):
    n=0 #未进位的
    f=0 #要进位的
    while b!=0:
        n=a^b 
        f=int(a&b)<<1
        a=n & 0xFFFFFFFF #最小值 负数； 0x7FFFFFFF 最大值正数
        b=f
    return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)

# incorrect in negative numbers if don't use unsigned int
def func(a,b):
    n=0 #未进位的
    f=0 #要进位的
    while b!=0:
        n=a^b 
        f=int(a&b)<<1
        a=n
        b=f
    return a

print(func(121,444))

def func(a,b):
   if (b==0): 
       return a
   return func(a^b,(a&b)<<1)

print(func(-1,2))

print(func(2,-1))

a=-1
b=2
        
        
        
        
        

















