#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:42:56 2022

@author: dantan
"""
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#  

# 示例 1：


# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# 输出：true
# 示例 2：


# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# 输出：false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


5*4

m*n
matrix=[[1,4,7,11],[2,5,8,12,19],[3,6,9,16],[10,13,14,17],[18,21,23,26]]
n=len(matrix) #5 row
m=len(matrix[0]) # 4 column


#
# 首先每行的元素从左到右升序排列，每列的元素从上到下升序排列，则从每一行最后一个元素开始查找，
# 若当前行最后的一个元素大于target，则查询向左移动，即列数减少一，若当前行的最后一个值小于target，则行数向下增加，即行数加一。

# 作者：jie-fang-qu-de-tian-0416
# 链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/tu-jie-by-jie-fang-qu-de-tian-0416/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix) # row
        n=len(matrix[0]) #column
        if n ==0:
            return False
        #if matrix==[]: return False
        i=0
        j=n-1
        while j>=0 and i<=m-1:
            if target<matrix[i][j]:
                j-=1
            elif target>matrix[i][j]:
                i+=1
            else:
                return True
        return False








