#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:49:38 2021

@author: dantan
"""
#Simple

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(word[::-1] for word in s.split(" "))
    

# can see each of the reverse word

class Solution:
    def reverseWords(self, s: str) -> str:
        s_split=s.split(" ")
        new_s=[[] for x in range(len(s_split))]
        for i in range(len(s_split)):
            each_word=s_split[i]
            for each_char in each_word[::-1]:
                new_s[i].append(each_char)
                if len(new_s[i])==len(each_word):
                    new_s[i].append(" ")
        new_s=[char for i in new_s for char in i]
        new_s.pop()
        new_s="".join(new_s)
        return new_s

# a = [1,3,6,8,9]
# print("通过下标逆序遍历1：")
# for i in a[::-1]:
#     print(i, end=" ")
# print("\n通过下标逆序遍历2：")
# for i in range(len(a)-1,-1,-1):
#     print(a[i], end=" ")
# print("\n通过reversed逆序遍历：")
# for i in reversed(a):
#     print(i, end=" ")


# for i in a:
#     for j in i:
#         print(j)

# b=[j for i in a for j in i]
        












