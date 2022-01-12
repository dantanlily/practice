#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:10:53 2022

@author: dantan
"""

from typing import List

#leetcode 98
# creating binary tree
class node():
    def __init__(self, k=None, l=None, r=None):
        self.val = k
        self.left = l
        self.right = r

def listcreattree(root,llist,i):###用列表递归创建二叉树，
# 它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
# 再接着创建b的右子树，
    if i<len(llist):
        if llist[i] ==None:
            return None ###这里的return很重要
        else:
            root=node(k=llist[i])
            print (i)
            root.left=listcreattree(root.left,llist,2*i+1)
            root.right=listcreattree(root.right, llist,2*i+2)
            return root### must have return for recursion； i changed back to 0 when tree is generated
    return root

if __name__ == '__main__':
    root=node()
    llist=[1,2,3,None,4,5]
    # set initial i =0, as root. Adjust following i to 
    root=listcreattree(root,llist,0) # set initial i =0, as root. Adjust following i to 

#############
root = [2,1,3]
root = [5,1,4,None,None,3,6]
# 1. 前序(Pre-order):根-左-右 
# 2. 中序(In-order):左-根-右  left root right 
# 3. 后序(Post-order):左-右-根

# for the binary tree in order -> array ascending 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
   def isValidBST(self,root):
    inorder=self.inorder(root)
    return inorder ==list(sorted(set(inorder))) 

   def inorder(self,root):
      if root is None:
          return [] 
      return self.inorder(root.left)+[root.val]+self.inorder(root.right)

# Method 2
def isValidBST(self,root):
    self.prev=None
    return self.helper(root)

def helper(self,root):
    if root is None:
        return True
    if not self.helper(root.left):
        return False
    if self.prev and self.prev.val >=root.val:
        return False
    self.prev = root
    return self.helper(root.right)
    

# recursion: validate (min max)
# max<-validate(node.left)
# min<-validate(node.right)
# max left <root min right >root

public bollean isValid(TreeNode root, Integer min, Integer max){
    if(root==null) return true;
    if (min!= null && root.val<=min) return false;
    if (max!= null && root.val>=max) return false;
    
    return isValid(root.left,min,root.val) &&
      isValid(root.right,root.val,max);
 
}





