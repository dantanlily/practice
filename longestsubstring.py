#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:53:46 2021

@author: dantan
"""


# Find longest substring without repeating characters


# Using dic m to store both new element value and positions 
#and locate last duplicate value location

from typing import List 
import time
start=time.time()

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        max_length=0
        m={}
        while(left<len(s) and right<len(s)):
            element=s[right]
            if (element in m):
                left=max(left,m[element]+1)
            m[element]=right
            max_length=max(max_length,right-left+1)
            right+=1
        return max_length
    
#create a instance
s=Solution()
answer=s.lengthOfLongestSubstring(["a","b","a","a","c","a","d"])
print(answer)
end=time.time()
print(end-start)  
        
x = 0
while x < 100:
    if x == 5: 
        break
    print(x)
    x+= 1     
        
      
x = 0
while x < 5: 
    if x == 1: 
        continue 
    print(x)
    x+= 1    # wrong infinite loop
     
x = 0
while x < 100:
    x+=1
    if x == 5: 
        continue
    print(x)
      
        
      
        










