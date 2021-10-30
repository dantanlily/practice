#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 19:14:19 2021

@author: dantan
"""

# 3 sum

from typing import List

# time limit exceeded error when input length is over 2000
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            print([])
        
        m=[]
        dict1={}
        for i,a in enumerate(nums):
            for j,b in enumerate(nums[i+1:]):
                if (-(a+b)) in dict1 and (i!= dict1.get(-(a+b)) and (j+i+1)!=dict1.get(-(a+b))):
                    m.append([nums[dict1.get(-(a+b))],nums[i],nums[i+j+1]])
                else:
                    dict1[a]=dict1.get(a,i)

        m=[tuple(sorted(item)) for item in m] # convert it to tuple then can use 'set'
        m=list(set(m)) # remove duplicates like [(-1, 0, 1), (-1, -1, 2), (-1, 0, 1)] using set. 
        m=[list(item) for item in m]
        
        return m

s=Solution()
s.threeSum([-1,0,1,2,-1,-4])

#[[-1, 0, 1], [-1, -1, 2]]

# correct method 1

nums=[-1,0,1,2,-1,-4]

def threeSum(nums):
    if len(nums)<3:
        return []
    nums.sort()
    res=set()
    for i,v in enumerate(nums[:-2]): # 3 nums
        if i>=1 and v==nums[i-1]: # duplicate loop again
            continue
        d={}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x]=1
            else:
                res.add((v,-v-x,x)) # res {(-1,0,1),(-1,-1,2)}
    return list(map(list,res)) #

threeSum(nums)


# method 2

def threeSum2(nums):
    res=[]
    nums.sort()
    for i in range(len(nums)-2): # xrange
        if i>0 and nums[i]==nums[i-1]:
            continue
        l,r=i+1,len(nums)-1
        while l<r:
            s=nums[i]+nums[l]+nums[r]
            if s<0:l+=1
            elif s>0:r-=1
            else:
                res.append((nums[i],nums[l],nums[r]))
                # duplicate
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                l+=1;r-=1
    return res

threeSum2(nums)            
            
        





# continue and pass comparison example

a = 'python'
i = 2
for element in a:
    if element == 'y':
        pass
        i = 3
    else:
        print(element+str(i))
 

# result 
# p2
# t3
# h3
# o3
# n3

a = 'python'
i = 2
for element in a:
    if element == 'y':
        continue
        i = 3
    else:
        print(element+str(i))
 
# result 
 
# p2
# t2
# h2
# o2
# n2



for i in range(0, 100):
    print(i)
    
for i in xrange(0, 100):
    print(i)












