#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:18:10 2023

@author: dantan
"""
# bag_size = 4
# weight = [1, 3, 4]
# value = [15, 20, 30]

# dp[i,j] [0-i] size[j] max value
#          max_size
#          0 1 2 3 4
# bag 0
#     1
#     2

def test_2_wei_bag_problem1(bag_size, weight, value):
    m,n=len(weight),(bag_size+1)
    dp=[[0 for _ in range(n)] for _ in range(m)]
    for j in range(weight[0],n):
        dp[0][j]=value[0]
    for i in range(1,m):
        for j in range(1,n):
            if weight[i]<=j:
                dp[i][j]=max(dp[i-1][j-weight[i]]+value[i],dp[i-1][j])
            else: 
                dp[i][j]=dp[i-1][j]
    print(dp[-1][-1])
# same
def test_2_wei_bag_problem1(bag_size, weight, value):
    m,n=len(weight),(bag_size+1)
    dp=[[0 for _ in range(n)] for _ in range(m)]
    for j in range(weight[0],n):
        dp[0][j]=value[0]
    for i in range(1,m):
        for j in range(1,n):
            if weight[i]>j:
                dp[i][j]=dp[i-1][j]
            else: 
                dp[i][j]=max(dp[i-1][j-weight[i]]+value[i],dp[i-1][j])
    print(dp[-1][-1])

# In[]
def test_2_wei_bag_problem1(bag_size, weight, value) -> int:
	rows, cols = len(weight), bag_size + 1
	dp = [[0 for _ in range(cols)] for _ in range(rows)]

	# 初始化dp数组.
	for i in range(rows):
		dp[i][0] = 0
	first_item_weight, first_item_value = weight[0], value[0]
	for j in range(1, cols):
		if first_item_weight <= j:
			dp[0][j] = first_item_value

	# 更新dp数组: 先遍历物品, 再遍历背包.
	for i in range(1, len(weight)):
		cur_weight, cur_val = weight[i], value[i]
		for j in range(1, cols):
			if cur_weight > j: # 说明背包装不下当前物品.
				dp[i][j] = dp[i - 1][j] # 所以不装当前物品.
			else:
				# 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight]+ cur_val)

	print(dp)


if __name__ == "__main__":
	bag_size = 4
	weight = [1, 3, 4]
	value = [15, 20, 30]
	test_2_wei_bag_problem1(bag_size, weight, value)