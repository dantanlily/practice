#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:29:04 2021

@author: dantan
"""

# group Anagrams (same letter different order)


from typing import List
class Solution:
    def findHash(self,s):
        return ''.join(sorted(s))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        m = {}

        for s in strs:
            hashed = self.findHash(s)
            if(hashed not in m):
                m[hashed] = []
            m[hashed].append(s)
        
        for p in m.values():
            answers.append(p)
        
        return answers

s=Solution()
answer=s.groupAnagrams(['tan','ant','cat','act'])
print(answer)
# [['tan', 'ant'], ['cat', 'act']]




# strs=['tan','ant','cat','act']

# answers=[]
# m={}

# for s in strs:
#     s_sorted_key=''.join(sorted(s))
#     if s_sorted_key not in m: # s_sorted is key, that use to match value later
#         m[s_sorted_key]=[]
#     m[s_sorted_key].append(s)

# for p in m.values():
#     answers.append(p)
    
# m.values() # dict_values([['tan', 'ant'], ['cat', 'act']])
