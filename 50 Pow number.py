#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 00:02:02 2022

@author: dantan
"""

from typing import List

#50 pow(x,n) 

# consider n <=0, odd/even number; find a way to normalise different scenarios

class Solution:
    def myPow(self,x,n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x,-n) # just reciprocal number, n is inverse, then it's the same 
        
        if n % 2:
            return x * self.myPow(x,n-1) 
        
        return self.myPow(x*x,n/2) # reduce as n/2 O (logn)


s=Solution()
s.myPow(2,10)

# method 2
class Solution:
    def myPow(self,x,n):
        if n<0:
            x=1/x
            n=-n
        pow=1
        while n:# while n>0:
            if n&1: # odd numberb last digit is 1; bitwise operators  #& 按位运算符，参与运算的两个值，如果相应位都为1，则该位的结果为1，否则为0
                pow*=x
            x*=x
            n>>=1 # a << =2 equal to a = a << 2; >>右移动运算符：把>>左边的运算数的各二进制位全部右移若干位，>> 右边的数字指定了移动的位数
        return pow

x=2 
n=10
s=Solution()
s.myPow(2,10)

# n=1 001; execute if; return x; done
# n=2 010; execute x*=x; execute if pow*=x return x^2 done
# n=3 011; 001; execute pow*x x=x^2 
# n=4 100; ....




