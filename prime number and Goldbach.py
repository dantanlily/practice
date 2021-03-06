#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:49:02 2021

@author: dantan
"""

#Given a positive integer n, calculate how many prime numbers are less than or equal to n. 
#For example, 17, it returns 7, because the prime numbers less than or equal to 7 
#are 2, 3, 5, 7, 13, 17


#Thoughts
#Consider till sqrt n is enough. Like 101, 100=10*10 9*11 9 was considered before
#start from minimum prime 2, then start makring false, 2*2,2*3,2*4...
#Others leaved as True, is prime number. 

#count_prime(10)


#n=10
#is_prime = [True] * (n + 1)
#i = 2
#while (i * i <= n):
#    if (is_prime[i]):
#        j = i
#        while (j * i <= n):
#            is_prime[i * j] = False
#           j += 1
#            print(i,j)
#    i += 1
    
#count how many 'True' 
#count = 0
#for i in range(2, n+1):
#    if (is_prime[i]):
#        count += 1
#        print(i,end = " ")


def count_prime(n):
    is_prime = [True] * (n + 1)
    i=2
    while (i*i<=n):
        if (is_prime[i]):
            j=i
            while (j*i<=n):
                is_prime[j*i]=False
                j+=1
        i+=1
    #count from 2, the minimum prime
    count=0
    for i in range(2,n+1):
        if(is_prime[i]): 
           count+=1
           print(i,end=" ")
    return count
  
count_prime(100)

#Any even number greater than 2 can be expressed as the sum of two prime numbers.
#Thoughts
#first find prime numbers within n range; then combine prime numbers together as a list
#finally use two pointers quickly add numbers up to see if it's a match


def goldbach(n):
    is_prime=[True]*(n+1)
    i=2
    while(i*i<=n):
        if (is_prime[i]):
            j=i
            while (j*i<=n):
                is_prime[j*i]=False
                j+=1
        i+=1
    
    count=0
    for i in range(2,n+1):
        if (is_prime[i]):
            count+=1
    
    primes=[None]*count
    idx=0
    for i in range(2,n+1):
        if (is_prime[i]):
            primes[idx]=i
            idx+=1
    
    left=0
    right=count-1
    while(left<right):
        if (n==primes[left]+primes[right]):
            print(n,"=",primes[left],"+",primes[right])
            left+=1
            right-=1
        elif (n>primes[left]+primes[right]):
            left+=1
        else:
            right-=1
        
    
goldbach(100)            



