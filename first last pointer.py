#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:21:34 2021

@author: dantan
"""

# Find first index and last index in a sorting array
"""nums=[10,11,11,11,14,15]
     
target=11
left=0
right=len(nums)-1
while(left<=right):
    mid=(left+right)//2
    if (nums[mid]==target and (nums[mid-1]!=target or mid==0)): 
        first_index=mid
        #print(first_index)
        break
    elif nums[mid]<=target:
        left+=1
    else:
        right-=1

print(first_index)"""

from typing import List

class Solution:
    
    def searchRange(self,nums: List[int],target: int)-> List[int]:
        left= self.getLeftPosition(nums,target)
        right=self.getRightPosition(nums,target)
        
        return[left,right]
    
    def getLeftPosition(self,nums,target):
        left=0
        right=len(nums)-1
        
        while(left<=right):
            
            mid=(left+right)//2
            if (nums[mid]==target):
                if (nums[mid-1]!=target or mid==0):
                    return mid
                right=mid-1
                
            elif nums[mid]<=target:
                left+=1
            else:
                right-=1
                
        return -1 # Value not found
            
    def getRightPosition(self,nums,target):
        left=0
        right=len(nums)-1
        
        while (left<=right):
            
            mid=(left+right)//2
            if (nums[mid]==target):
                if (nums[mid+1]!=target or mid==len(nums)-1):
                    return mid
                left=mid-1
            elif nums[mid]<=target:
                left+=1
            else:
                right-=1
        return -1

s=Solution()
answer=s.searchRange([10,11,11,11,14,15],11)
print(answer)











