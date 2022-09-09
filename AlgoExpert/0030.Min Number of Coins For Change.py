#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:10:21 2022

@author: dantan
"""

# Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, implement a
# function that returns the smallest number of coins needed to make change for that target amount using the given coin denominations. Note that an unlimited
# amount of coins is at your disposal. If it is impossible to make change for the target amount, return -1.

# Sample input: 7, [1, 5, 10]

# Sample output: 3 (2x1 + 1x5)



# first fill all nums[amount] using the first denoms, 
# then go through all denoms and compare with the previous obtained value

# o(nd) time|o(n) space
def minnumberOfCoinsForChange(n,denoms):
    numOfCoins=[float("inf") for amount in range(n+1)]
    numOfCoins[0]=0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <=amount:
                numOfCoins[amount]=min(numOfCoins[amount],numOfCoins[amount-denom]+1)   

    return numOfCoins[n] if numOfCoins[n]!=float("inf") else -1

minnumberOfCoinsForChange(6,[1,2,4])




