#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:25:40 2021

@author: dantan
"""

#
#https://leetcode.com/problems/valid-parentheses/submissions/

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
#determine if the input string is valid.

# Valid Parentheless

from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        paren_map={')':'(',']':'[','}':'{'}
        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif not stack or paren_map[c]!=stack.pop(): # pop() delete the last value
                return False
        return not stack

s=Solution()
s.isValid("()[]{}")



