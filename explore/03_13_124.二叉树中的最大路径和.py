#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:35:26 2023

@author: dantan
"""

# In[] C++
class Solution {
    int ans=INT_MIN;
public:
    int maxPathSum(TreeNode* root) {

        oneSideMax(root);
        return ans;
    }
    int oneSideMax(TreeNode* root){
        if (root ==nullptr) return 0;
            
        int left=max(0,oneSideMax(root->left));
        int right=max(0,oneSideMax(root->right));

        ans= max(ans,left+right+root->val);// only in final answer, plus root->val
        return max(left,right)+root->val;
    }
    
};
    
# In[] Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.oneSideMax(root)
        return self.ans

    def oneSideMax(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = max(0, self.oneSideMax(root.left))
        right = max(0, self.oneSideMax(root.right))

        self.ans = max(self.ans, left + right + root.val)  # only in final answer, plus root->val
        return max(left, right) + root.val




