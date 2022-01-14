#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:48:35 2022

@author: dantan
"""

#236 Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root==None or root==p or root ==q): # if root in [p, q, None]
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left!=None and right!=None: # if left and right; elif right; elif left
            return root
        elif left==None and right!=None:
            return right
        else:
            return left

#235 Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root # must added for p and q not in the same side
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val > q.val:
                root=root.left
            elif p.val > root.val < q.val:
                root=root.right
            else:
                return root
    
    