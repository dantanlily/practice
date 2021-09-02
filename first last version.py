#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:41:29 2021

@author: dantan
"""

# The isBadVersion API is already defined for you.
# @param version,an integer
# @return a book
# def isBadVersion(version)

def isBadVersion(version):
    first_bad_version=3
    return version>=first_bad_version

# isBadVersion(2) False
# Find first bad version
class Solution:
    def firstBadVersion(self,n):
        """
        :type n:int
        :rtype: int
        """
        left=1
        right=n
        
        while(left<right):
            
            #mid=left+(right-left)//2
            mid=(left+right)//2
            if not isBadVersion(mid): # if mid is Good version
                left=mid+1
            else:
                right=mid-1
                
        return left
        
s=Solution()
answer=s.firstBadVersion(10)
print(answer)





