#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:20:47 2023

@author: dantan
"""

from typing import List,Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder,preStart, preEnd, inorder, inStart, inEnd) -> TreeNode:
            # important to have base case, otherwise raise error
            if preStart > preEnd:
                return None
            
            rootVal=preorder[preStart]
            # rootVal在中序遍历数组中索引
            index=0
            for i in range(inStart,inEnd+1):
                if inorder[i]==rootVal:
                    index=i
                    break
            root=TreeNode(rootVal)
            #递归构造左右子树
            root.left=build(preorder,preStart+1,preStart+(index-inStart),\
                            inorder,inStart,index-1)
            root.right=build(preorder,preStart+(index-inStart)+1,preEnd,\
                             inorder,index+1,inEnd)
            return root
        return build(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)

s=Solution()
s.buildTree([3,9,20,15,7],[9,3,15,20,7])

# In[] use hash table quicker no need to using for loop to find index
valToIndex={}
def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    for i in range(len(inorder)):
        valToIndex[inorder[i]] = i
    # 根据函数定义，用 preorder 和 inorder 构造二叉树
    return build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

# build 函数的定义：若前序遍历数组为 preorder[preStart..preEnd]，中序遍历数组为 inorder[inStart..inEnd]，构造二叉树，返回该二叉树的根节点
def build(preorder: List[int], preStart: int, preEnd: int, inorder: List[int], inStart: int, inEnd: int) -> TreeNode:
        
    if preStart > preEnd:
        return None

    # root 节点对应的值就是前序遍历数组的第一个元素
    rootVal = preorder[preStart]
    # rootVal 在中序遍历数组中的索引
    index = valToIndex.get(rootVal)

    leftSize = index - inStart

    # 先构造出当前根节点
    root = TreeNode(rootVal) 

    # 递归构造左右子树
    root.left = build(preorder, preStart + 1, preStart + leftSize,
                      inorder, inStart, index - 1)

    root.right = build(preorder, preStart + leftSize + 1, preEnd,
                       inorder, index + 1, inEnd)
    return root

t=buildTree([3,9,20,15,7],[9,3,15,20,7])
t.val # 3
t.left.val
t.left
