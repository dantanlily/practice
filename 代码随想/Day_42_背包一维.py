#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:08:35 2023

@author: dantan
"""

for j in range(4,1,-1):
    print(j)
# 4, 3, 2 # 起始点都能遇到 到终点边界前一个 


def test_1_wei_bag_problem(weight, value, bagWeight):
    # 初始化
    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):  # 遍历物品
        for j in range(bagWeight, weight[i] - 1, -1):  # 遍历背包容量
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    return dp[bagWeight]


if __name__ == "__main__":

    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    result = test_1_wei_bag_problem(weight, value, bagweight)
    print(result)


# In[] my own


def bag1_problem(weight,value,bagweight):
    #初始化 有4个背包 最后dp[j]表示容量为j的背包可以装的最大容量
    dp=[0]*(bagweight+1)
    for i in range(len(weight)): #物品
        for j in range(bagweight,weight[i]-1,-1): 
            dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
            print(i,j,dp[j])
    print(dp[j])
        
'''
dp[j-weight[i]+value[i]  容量为j的背包想再放一个物品i 那么要确保容量j能够放 减去物品
i的重量 不影响之前的j之前已经放进去的价值 并且留出来再放i物品的容量
和之前的dp[j]进行比较 

想自然过程 倒序遍历背包 从容量最大的开始 不影响之前的值覆盖 
想process遍历过程

max(dp[j],dp[j-weight[i]]+value[i])

第一个dp[j]相当于不放物品j 相当于用上一个

物 量 值
0 4 15
0 3 15
0 2 15
0 1 15
1 4 35
1 3 20
2 4 35

容量为4  装物0 物1时候价值就已经35了 
容量为4  装物2的时候 dp[0]+30 = 30 和之前的装容量1 2的时候35 比 少了 
容量4最终还是35

'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    