#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:58:07 2022

@author: dantan
"""

# Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, implement a
# function that returns the number of ways to make change for that target amount using the given coin denominations. Note that an unlimited amount of coins is at
# your disposal.

# Sample input: 6, [1, 5]

# Sample output: 2 (1x1 + 1x5 and 6x1)
  
# o(nd) time|o(n) space
# amount from 0 to n, loop each denoms to see how many ways for each amount
def numberOfWaysToMakeChange(n,denoms):
    ways=[0 for i in range(n+1)]
    ways[0]=1 
    for denom in denoms:
        for amount in range(1,n+1):
            ways[amount]+=ways[amount-denom] 
    return ways[n]

numberOfWaysToMakeChange(6,[1,5])



