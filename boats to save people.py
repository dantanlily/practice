#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:15:56 2021

@author: dantan
"""

# Given an array people and an integer limit 
# people arrayis people's weight and each bot can carry at mostl limit
# Each boat carries at most 2 people at the same time
# return the minumum number of boats to carry every given person


from typing import List 

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat=0
        left=0
        right=len(people)-1
        
        if max(people)>limit:
            print("error: max individual weight is bigger than boat limit")
            
        else:
            print(max(people))
            while left<=right:
                if left==right:
                    boat+=1
                    break
                if people[left]+people[right]<=limit:
                    left+=1
                right-=1
                boat+=1 
        return boat

        

#create a instance
s=Solution()
answer=s.numRescueBoats([2,1,3,4],4)
print(answer)

answer=s.numRescueBoats([2,1,3,5],4)