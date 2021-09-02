#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:31:54 2021

@author: dantan
"""

# Count/Print Composite or Prime number

# Method 1
import math
class Solution:
    def countPrimes(self,n):
        list_Composite=[]
        if (n<2):
            return 0
        isPrime=[True]*n
        isPrime[0]=isPrime[1]=False
        
        for i in range(2,int(math.ceil(math.sqrt(n)))): #int(math.ceil(math.sqrt(n)
            if (isPrime[i]):
                for multiples_of_i in range(i*i,n,i): # step is i , same as multiple 
                    isPrime[multiples_of_i]=False
                    list_Composite.append(multiples_of_i) # composite number
        
        
        list_Primes=[None]*sum(isPrime)
        idx=0
        for j in range(2,len(isPrime)):
            if isPrime[j]:
                list_Primes[idx]=j
                idx+=1
                
        return sum(isPrime),list_Composite,list_Primes
    
s=Solution()
answer=s.countPrimes(12) #2，3，5，7，11; 5 numbers in total 
print(answer)


# Method 2
class Solution:
    def count_prime(self,n):
        isPrime=[True]*(n+1)
        i=2 # start from 2
        while(i*i<=n):
            if(isPrime[i]):
                j=i # reset j based on i
                while(j*i<=n):
                    isPrime[j*i]=False
                    j=j+1
            i+=1
        
        # count
        count=0
        for i in range(2,n+1):
            if(isPrime[i]):
                count+=1
                
        primes=[None]*count
        idx=0
        for i in range(2,n+1):
            if (isPrime[i]):
                primes[idx]=i
                idx+=1    
                
        return count,primes
    
    
        
s=Solution()
answer=s.count_prime(12) #2，3，5，7，11; 5 numbers in total 
print(answer)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        