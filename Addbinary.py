#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:34:54 2021

@author: dantan
"""

# Sum of binary number
# Rule

# a, b , result , carry 
# 0, 0, 0, 0
# 1, 0, 1, 0
# 0, 1, 1, 0
# 1, 1, 0 ,1

# result sum(digit a, digit b)%2
# carry  sum(digit a, digit b)//2

class Solution(object):
    
    def addBinary(self, a, b):
        result=[]
        carry=0
        i=len(a)-1
        j=len(b)-1
        
        while i>=0 or j>=0 or carry:
            total=carry
            
            if i>=0:
                total+=int(a[i])
                i-=1
                
            if j>=0:
                total+=int(b[j])
                j-=1
            
            result.append(str(total%2))
            carry=total//2
                
     
        return ''.join(reversed(result))

#  110
#  010
#1 000

s=Solution()
answer=s.addBinary("110","010")
print(answer)
