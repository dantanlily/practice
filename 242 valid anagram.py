#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:15:24 2021

@author: dantan
"""

#Given two strings s and t, return true if t is an anagram of s, and false otherwise.


s = "anagram"
t = "nagaram"
# O(n*log n)
def isAnagram3(s,t):
    return sorted(s)==sorted(t)

#
person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))

print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))

#
# Name:  Phill
# Age:  22
# Salary:  None
# Salary:  0.0

# 


def isAnagram2(s,t):
    dict1,dict2=[0]*26,[0]*26
    for item in s:
        dict1[ord(item)-ord('a')]+=1
    for item in t:
        dict2[ord(item)-ord('a')]+=1
    return dict1==dict2

#ord('a') # 97

# 
def isAnagram1(s,t):
    dict1,dict2={},{}
    for item in s:
        dict1[item]=dict1.get(item,0)+1
    for item in t:
        dict2[item]=dict2.get(item,0)+1
    return dict1==dict2
        
    






