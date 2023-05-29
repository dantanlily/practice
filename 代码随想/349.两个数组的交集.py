#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:25:05 2023

@author: dantan
"""

'''
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是唯一的。我们可以不考虑输出结果的顺序 。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
 

提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''

#注意题目特意说明：输出结果中的每个元素一定是唯一的，也就是说输出的结果的去重的， 
# 同时可以不考虑输出结果的顺序


#table = {}
# for num in nums1:
#     table[num] = table.get(num, 0) + 1


nums1 = [1,2,2,1] 
nums2 = [2,2]


nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]
def intersection(nums1, nums2):
    nums_dic={}
    common={}
    l=[]
    #如果common是list append没有去重功能 返回的是[2,2]
    for i in range(len(nums1)):
        nums_dic[nums1[i]]=1
    for j in range(len(nums2)):
        if nums2[j] in nums_dic:
            common[nums2[j]]=1
    [l.append(key) for key in common.keys()]
    return l
   

intersection(nums1, nums2)

# In[]
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))         
    #          list(set(nums1) & set(nums2))
    
# In[]   
    
 class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)   
    
    
# In[]
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0]*1001
        count2 = [0]*1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]]+=1
        for j in range(len(nums2)):
            count2[nums2[j]]+=1
        for k in range(1001):
            if count1[k]*count2[k]>0:
                result.append(k)
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    