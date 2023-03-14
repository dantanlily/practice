#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 10:21:15 2023

@author: dantan
"""

# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码还未经过力扣测试，仅供参考，如有疑惑，可以参照我写的 java 代码对比查看。

from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums:List[int]) ->TreeNode:
            if not nums:
                return None
    
            # 找到数组中的最大值
            maxVal = max(nums)
            index = nums.index(maxVal)
            
            root = TreeNode(maxVal)
            # 递归调用构造左右子树
            root.left = build(nums[:index])
            root.right = build(nums[index+1:])

            return root
        return build(nums)

# def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
#     if not nums:
#         return None
    
#     # 找到数组中的最大值
#     maxVal = max(nums)
#     index = nums.index(maxVal)
    
#     root = TreeNode(maxVal)
#     # 递归调用构造左右子树
#     root.left = constructMaximumBinaryTree(nums[:index])
#     root.right = constructMaximumBinaryTree(nums[index+1:])
    

#     return root


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    return build(nums)

def build(nums:List[int]) ->TreeNode:
    if not nums:
        return None
    
    # 找到数组中的最大值
    maxVal = max(nums)
    index = nums.index(maxVal)
    
    root = TreeNode(maxVal)
    # 递归调用构造左右子树
    root.left = build(nums[:index])
    root.right = build(nums[index+1:])
    

    return root

nums=[3,2,1,6,0,5]
tree=constructMaximumBinaryTree(nums)
constructMaximumBinaryTree(nums).val # 6
constructMaximumBinaryTree(nums).left.val # 3
constructMaximumBinaryTree(nums).right.val # 5

constructMaximumBinaryTree(nums).left.right.val # 2s

# In[]
from binarytree import tree,Node

print(tree(height=3, is_perfect=False, letters=True))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)

print(root)

# In[]

'''
max(enumerate(nums[0:len(nums)+1]), key=lambda x: x[1]) is a Python expression that returns a tuple containing the index and the maximum value in a given list nums.

Here's a breakdown of the expression:

enumerate(nums[0:len(nums)+1]) creates an iterator that generates a tuple of (index, value) pairs for each element in the list nums from index 0 up to and including the last index len(nums).

key=lambda x: x[1] specifies a function that takes a tuple of (index, value) pairs and returns the value of the tuple's second element, i.e., the value of the corresponding element in the list nums. This is used to determine the maximum value among all the values in the list.

max() returns the tuple (index, maxVal) with the highest value of maxVal according to the key function.

Therefore, the overall effect of the expression is to return a tuple containing the index and the maximum value in the given list nums.
'''
index, maxVal = max(enumerate(nums[0:len(nums)]), key=lambda x: x[1])

# In[] slow method find max and index using a loop
class Solution:

    def build(self,nums: List[int], lo: int, hi: int) -> TreeNode:
        # base case
        if lo > hi:
            return None

        # 找到数组中的最大值和对应的索引
        index, maxVal = -1, -sys.maxsize
        for i in range(lo, hi+1):
            if maxVal < nums[i]:
                index = i
                maxVal = nums[i]

        # 先构造出根节点
        root = TreeNode(maxVal)
        # 递归调用构造左右子树
        root.left = self.build(nums, lo, index - 1)
        root.right = self.build(nums, index + 1, hi)
        
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)

# using self. 
    
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)

    def build(self,nums: List[int], lo: int, hi: int) -> TreeNode:
        # base case
        if lo > hi:
            return None

        # 找到数组中的最大值和对应的索引
        index, maxVal = -1, -sys.maxsize
        for i in range(lo, hi+1):
            if maxVal < nums[i]:
                index = i
                maxVal = nums[i]

        # 先构造出根节点
        root = TreeNode(maxVal)
        # 递归调用构造左右子树
        root.left = self.build(nums, lo, index - 1)
        root.right = self.build(nums, index + 1, hi)
        
        return root    
    
    
    








