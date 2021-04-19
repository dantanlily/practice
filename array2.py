#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 23:31:50 2021

@author: dantan
"""
#Coupon Collector
#Suppose that you have a shuffled deck of cards and you turn them face up, one by one. 
#How many cards do you need to turn up before you have seen one of each suit? Given N distinct card types, 
#how many random cards do you need do collect before you have (at least) one of each type?

#random.randint(a, b)
#Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

#Thoughts simulation until find n distinct

import random
def coupon(n):
    found=[False]*n
    count=0
    distinct=0
    while (distinct<n):
        val=random.randint(0,n-1)
        if (not found[val]):
            distinct+=1
            found[val]=True
        count+=1
    print(count)
    
coupon(10)
        

#1-bit and 2-bit Characters
#Ex9：1-bit and 2-bit Characters We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
#Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

#Example 1:
#Input: bits = [1, 0, 0]
#Output: True
#Explanation: The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

#Example 2:
#Input: bits = [1, 1, 1, 0]
#Output: False
#Explanation: The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.


def oneEnd(bits):
    i=0
    while i<len(bits)-1:
        i+=bits[i]+1
        print(i)
    return i==len(bits)-1 and bits[i]==0 

bits=[1,0,0]
print(oneEnd(bits))
bits=[1,1,1,0,1]
print(oneEnd(bits))











