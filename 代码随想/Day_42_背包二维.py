#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:54:00 2023

@author: dantan
"""

def test_2_wei_bag_problem1(weight, value, bagweight):
    # 二维数组
    dp = [[0] * (bagweight + 1) for _ in range(len(weight))]

    # 初始化
    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]

    # weight数组的大小就是物品个数
    for i in range(1, len(weight)):  # 遍历物品
        for j in range(bagweight + 1): # 遍历背包容量
        
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

    return dp[len(weight) - 1][bagweight]

if __name__ == "__main__":
    # row 背包重量weights
    # column 背包最大重量从0到4 index
    # dp[i][j] 从0-i个背包里随意装 最大容量为j的 能放多少
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    result = test_2_wei_bag_problem1(weight, value, bagweight)
    print(result)





# In[] my own
weight = [1, 3, 4]
value = [15, 20, 30]
bagweight = 4
#想图
def bag_problem(weight,value,bagweight):
    dp=[[0]*(bagweight+1) for _ in range(len(weight))]
    for j in range(weight[0],bagweight+1):
        dp[0][j]=value[0]
    
    # row 0 is already assigned 装第一个物品 index0 多少重量不同的背包j所能装的最大values
    for i in range(1,len(weight)):
        for j in range(bagweight+1):
            if j<weight[i]:
                dp[i][j]=dp[i-1][j]
            else:
                #考虑前i个背包 如何由前一个状态推导出来  不装；装的前提 （前一个状态来 把i的weight留出来）
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
            
    print(dp[len(weight)-1][bagweight])









