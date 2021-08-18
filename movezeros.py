#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 20:59:06 2021

@author: dantan
"""
from typing import List

class Solution:
    def moveZeros(self,nums:List[int]):
        j=0
        for num in nums:
            if (num !=0):
                nums[j]=num
                j+=1 # only count j when num!=0
            
        for i in range(j,len(nums)):
            nums[i]=0
        print(nums)
        
    
#create instance
s=Solution()
s.moveZeros([0,2,0,1,4])

nums=[0,2,0,1,4]