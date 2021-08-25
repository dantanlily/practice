#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:04:08 2021

@author: dantan
"""
#
#Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

#The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_number=min(nums)
        max_number=max(nums)
        for i in range(1,min_number+1):
            if((min_number%i==0) and (max_number%i==0)):
                GCD=i
        return GCD
