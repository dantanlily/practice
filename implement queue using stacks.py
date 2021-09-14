#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:36:06 2021

@author: dantan
"""

# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
        res = self.stack2.pop()
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # print self.stack1, self.stack2
        if not self.stack2:
            while self.stack1:
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2






