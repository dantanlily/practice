#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:06:54 2022

@author: dantan
"""

# We are given two arrays of integers array and sequence. We are asked to implement a function that is going to check whether all the numbers in the sequence appear in the array and they appear in the same order. In other words, the function needs to find out if we can get the sequence array from the array, when we delete some or no elements in the array without changing the order of the remaining elements.

# Example:

# array: [3, 1, 7, 5, 10, 2];
# sequence: [1, 5, 2];
# Output: true

# In[]
#o(n) time | o(1) space

def validatesubsequence(array,sequence):
    arrIdx=0
    seqIdx=0
    while arrIdx<len(array) and seqIdx<len(sequence):
        if array[arrIdx]==sequence[seqIdx]:
            seqIdx+=1
        arrIdx+=1
    return seqIdx==len(sequence)
        
        
# In[]
#o(n) time | o(1) space

def validatesubsequence(array,sequence):
    seqIdx=0
    for value in array:
        if seqIdx==len(sequence):
            break
        if sequence[seqIdx]==value:
            seqIdx+=1
    return seqIdx==len(sequence)

# In[]            
            
            
validatesubsequence([3, 1, 7, 5, 10, 2],[1,5,2])
            
            

        
    