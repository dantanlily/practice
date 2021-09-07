#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:29:55 2021

@author: dantan
"""
# Whether contains a duplicate 
# Method 1
from typing import List
class Solution:
    def containDuplicate(self,nums:List[int])-> bool: 
        m={} # for value store 
        for num in nums:
            if num in m:
                return True
            m[num]=1 # or m[num]=num or m[num]=1...just for occupying value purpose
        return False

s=Solution()
answer=s.containDuplicate([2,2,1,3])
print(answer)

# Method 2 

from collections import defaultdict
class Solution:
    def containDuplicate(self,nums:List[int])-> bool: 
        m=defaultdict(int)
        for num in nums:
            if(m[num]):
                return True
            m[num]+=1 # or m[num]=1 # occupying value purpose
        return False
    
s=Solution()
answer=s.containDuplicate([2,2,1,3])
print(answer)

