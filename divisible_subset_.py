#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:33:21 2021

@author: dantan
"""

#
#https://leetcode.com/problems/largest-divisible-subset/solution/


# use key as nums, to save all previous values

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num]=max([subsets[k] for k in subsets if num % k ==0], key=len) | {num}
            
            #  using '|' as append, only add next num when num % previous num (k) ==0
            #  using 'max( , key =len)' to find the 
            #  start with subsets key = -1; can then append any first num
            #  using one line loop, add '[]'
            #  example [set(), {1}, {1, 2}, {1, 3}, {1, 3, 9}, {1, 3, 9, 18}, {1, 3, 9, 18, 90}]
            
        
        return list(max(subsets.values(), key=len))

# nums=[9,75,12,18,90,4,36,8,28,2]
# subsets = {-1: set()}
# for num in sorted(nums):
#     subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
# print(list(max(subsets.values(), key=len)))


# for k in subsets:
#     print(k)

# Try 1: Slow-exceed time limit in large number
# nums=[1]

# nums=[1,2,3]

# nums=[546,669]

# nums=[3,4,16,8]

# nums=[4,8,10,240]

# nums=[1,2,3,4,6,24]

# nums=[2,3,5,7,11,13,17,19,23,31,1000000007]

from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if len(nums)==1:
            return nums
        else:
            
            input_nums=nums.copy()
            if 1 in nums:
                nums.remove(1)
                nums.sort()

            output={}
            for i in range(len(nums)):
                j=1
                if i not in output:
                    output[i]=[]
                if 1 in input_nums:
                    output[i].append(1)
                while(j*nums[i]<=max(nums)): 
                    try:
                        if (j*nums[i] in nums and (j*nums[i] % (output.get(i)[-1]))==0): 
                            output[i].append(j*nums[i])
                        j+=1 # position inside while loop
                    except:
                        if (j*nums[i] in nums): 
                            output[i].append(j*nums[i])
                        j+=1 # position inside while loop

            print_list=output.get(0)
            for key in output:
                if len(output.get(key))>len(print_list):
                       print_list=output.get(key)

            return print_list



# Try 2 use prime to find, not work in [4,8,10,240]
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if len(nums)==1:
                return nums
        if len(nums)==2:
            nums.sort()
            if nums[1]%nums[0]==0:
                return nums
            return [nums[0]]
        else:
            #common_prime=list(set(self.prime_list(nums)).intersection(set(nums)))
            prime=self.prime_list(nums)
            if len(prime)==0:
                return [nums[0]]
            else:
                output={}
                
                # value not include 1  
                for i in range(len(prime)):
                    j=0
                    if i not in output:
                        output[i]=[]
                    if 1 in nums:
                        output[i].append(1)
                    while(j*prime[i]<=max(nums)): 
                        if (j*prime[i] in nums):
                            output[i].append(j*prime[i])
                        j+=1 # position inside while loop
                
                print_list=output.get(0)
                for key in output:
                    if len(output.get(key))>len(print_list):
                           print_list=output.get(key)
                return print_list
    
    def prime_list(self, nums):
        n=max(nums)
        isPrime=[True]*n # the range of numbers
        isPrime[0]=False # 1 is not Prime
        i=2
        while(i*i<=n):
            j=i
            while(j*i<=n):
                isPrime[j*i-1]=False  # position j*i -1 
                j+=1
            i+=1
        
        prime_index=([i for i,x in enumerate(isPrime) if x==True]) # index for Prime number 
        consecutive_list =[i for i in range(1,max(nums)+1)]
        # Prime numbers
        prime_num=[consecutive_list[prime_index[i]] for i in range(len(prime_index))]
        return prime_num

s=Solution()
s.largestDivisibleSubset([4,8,10,240])


# Try 3

from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        #  compare the two lists 
        else:
            if len(self.cal(nums)[0])>=len(self.cal(self.cal(nums)[1])[0]):
                return self.cal(nums)[0]
            return self.cal(self.cal(nums)[1])[0]
    
    def cal(self,nums):
        output={}
        nums_update=nums.copy()
        nums.sort()
        for i in range(len(nums)):
            j=i
            
            if i not in output:
                output[i]=[]
                
            #if 1 in input_nums:
            #    output[i].append(1)
                
            while (j<=len(nums)-1):
                try:
                
                    if (nums[j]%nums[i]==0 and (nums[j] % (output.get(i)[-1]))==0): 
                        output[i].append(nums[j])
                    
                    j+=1
                    
                except:
                    
                    if nums[i]%nums[j]==0 : 
                        output[i].append(nums[j])
                        
                    j+=1
                        
            print_list=output.get(0)
            
        for key in output:
            if len(output.get(key))>len(print_list):
                   print_list=output.get(key)
        
        return print_list,nums_update

s=Solution()
nums=[5,9,18,54,108,540,90,180,360,720]

nums=[9,75,12,18,90,4,36,8,28,2]
s.largestDivisibleSubset([9, 18, 54, 90, 108, 180, 360, 540, 720])
s.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720])
s.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720])

s.cal([5,9,18,54,108,540,90,180,360,720])


nums=[9,75,12,18,90,4,36,8,28,2]
nums=sorted(nums)
print(nums)
#[2, 4, 8, 9, 12, 18, 28, 36, 75, 90]

nums=[1,2,3,4]
subsets = {-1: set()}
num=1
num=2
num=3
num=4

nums=8

# use key as nums, to save all previous values
for num in sorted(nums):
    subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
print(list(max(subsets.values(), key=len)))


for k in subsets:
    print(k)
    

mylist = ['123','123456','1234']
print (max(mylist, key=len))
#123456


    
    














