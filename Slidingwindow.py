#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 09:38:56 2021

@author: dantan
"""

# Brtue search of K consective elements

#Arr,K

def bruteSearch(arr,k):
    max_consective_sum=-99999999
    for i in range(len(arr)-k+1):# 0,1,2
        current_sum=0
        for j in range(k):# 0,1
            current_sum+=arr[i+j]
            max_consective_sum=max(max_consective_sum,current_sum)
    return max_consective_sum
        
arr = [80,-50,90,100]
k = 2

result = bruteSearch(arr,k)

# Sliding Search
#k= window size

def slidingSearch(arr,k):
    if(len(arr)<=k):
        print("Invalid operation")
        return -1
    
    window_sum=sum([arr[i] for i in range(k)])
    max_sum=window_sum
    i=0
    while i<(len(arr)-k):
        window_sum=window_sum-arr[i]+arr[i+k]
        max_sum=max(max_sum,window_sum)
        i+=1
    return max_sum
      

arr = [80,-50,90,100]
k = 2

result = slidingSearch(arr,k)
        

# Code Answer

def maxSum(arr, windowSize):
    arraySize = len(arr)
    # n must be greater than k
    if arraySize <= windowSize:
        print("Invalid operation")
        return -1

    # Compute sum of first window of size k
    window_sum = sum([arr[i] for i in range(windowSize)])
    max_sum = window_sum
    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    for i in range(arraySize-windowSize):
        window_sum = window_sum - arr[i] + arr[i + windowSize]
        max_sum = max(window_sum, max_sum)

    return max_sum


arr = [1, 2, 100, -1, 5]
# maximum sum should be 104 => 100 + -1 + 5
answer = maxSum(arr, 3)
print(answer)

for i in range(0,2):
    print (i)


    
    
    
    
    
    
    