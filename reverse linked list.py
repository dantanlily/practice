#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:44:30 2021

@author: dantan
"""

#Given the head of a singly linked list, reverse the list, and return the reversed list.
#https://leetcode.com/problems/reverse-linked-list/
# Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur,prev=head,None
        while cur:
            cur.next,prev,cur=prev,cur,cur.next
        return prev

#https://leetcode.com/problems/linked-list-cycle/
#Given head, the head of a linked list, determine if the linked list has a cycle in it.
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
#Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast=slow=head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow is fast:
                return True
        return False
    

#Swap Nodes in Pairs
#https://leetcode.com/problems/swap-nodes-in-pairs/
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre,pre.next=self,head
        while pre.next and pre.next.next:
            a=pre.next
            b=a.next
            pre.next,b.next,a.next=b,a,b.next
            pre=a
        return self.next
