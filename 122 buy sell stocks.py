#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:32:27 2022

@author: dantan
"""

# 122

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. 
#You can only hold at most one share of the stock at any time. 
#However, you can buy it then immediately sell it on the same day.


# assumptions: all day prices are foreseeable. no transcation cost; no short; 1 share

# greedy algorithm O(n) if next day is larger than today, then buy today, sell tomorrow

# DP can solve more complex problem,. Decision is not only based on current situation, but overall results

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                max_profit+=prices[i+1]-prices[i]
        return max_profit

s=Solution()
s.maxProfit([7,1,5,3,6,4])


# prices=[7,1,5,3,6,4]
# prices=[1,2,3,4,5]
# prices=[7,6,3,2]
# max_profit=0
# for i in range(len(prices)-1):
#     if prices[i+1]>prices[i]:
#         max_profit+=prices[i+1]-prices[i]


# DFS depth-first seatch; ry buy 1 share/sell 1 share on same day O(2^n) depth first search
# DP  dynamic programming
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        for i, price in enumerate(prices):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -price
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
                
        return dp[len(prices) - 1][0] if prices else 0
    

# prices=[1,2,3] 
# dp = [[0 for _ in range(2)] for _ in range(len(prices))] every day has two prices saved (yesterday)
# for i, price in enumerate(prices):
#     if i == 0:
#         dp[0][0] = 0
#         dp[0][1] = -price
#     else:
#         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
#         dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])    
        





    
    
    