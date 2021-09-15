#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:12:14 2021

@author: dantan
"""
# sorting

def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selectionSort(arr):
    sort_Arr=[]
    for i in range(len(arr)):
        current_smallest=findSmallest(arr) # current_smallest is the index of the smallest number
        sort_Arr.append(arr.pop(current_smallest)) # pop find value based on index, and then delete value
    return sort_Arr
    

print(selectionSort([5,3,6,2,10]))