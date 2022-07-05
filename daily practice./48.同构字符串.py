#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 08:54:04 2022

@author: dantan
"""
# 205. 同构字符串
# 给定两个字符串 s 和 t ，判断它们是否是同构的。

# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

# 示例 1:

# 输入：s = "egg", t = "add"
# 输出：true
# 示例 2：

# 输入：s = "foo", t = "bar"
# 输出：false
# 示例 3：

# 输入：s = "paper", t = "title"
# 输出：true
 

# 提示：

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s 和 t 由任意有效的 ASCII 字符组成

s = "egg"
t = "add"

s='badc'
t="baba"
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        dic1={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=[]
            if t[i] not in dic1:
                dic1[t[i]]=[]
            dic[s[i]].append(t[i])
            dic1[t[i]].append(s[i])
            if len(set(dic.get(s[i])))>1 or len(set(dic1.get(t[i])))>1:
                return False
        return True

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = dict()
        for i, char in enumerate(s):
            if char in mapping:
                if mapping[char] != t[i]: #一对多
                    return False
            else:
                if t[i] in mapping.values(): #多对一
                    return False
                mapping[char] = t[i]
        return True
        

# set(list(dic.values()))

# len(set(dic.get(s[i])))





