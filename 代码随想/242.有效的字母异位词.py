#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:33:56 2023

@author: dantan
"""
'''
242. 有效的字母异位词
简单
785
相关企业
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
 

提示:

1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母
'''

s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

s='a'
t='ab'
#是次数相同
#第二个循环j in range 不要忘记第二个else判断 比如a ,ab 类似发生 
#t元素不在s中 直接判断false

def isAnagram(s,t):
    s_dic={}
    for i in range(len(s)):
        if s[i] in s_dic: 
            s_dic[s[i]]+=1
        else:
            s_dic[s[i]]=1
    for j in range(len(t)):
        if t[j] in s_dic:
            s_dic[t[j]]-=1
        else:
            return False   # important to add 
    for value in s_dic.values(): 
        if value!=0:
            return False
    return True
        

isAnagram(s,t)

# In[]
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1
        
        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict  
# In[] 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True


    
# In[]   
from collections import Counter
a_count = Counter(s)    #Counter({'a': 1})


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    