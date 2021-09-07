#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:53:41 2021

@author: dantan
"""

#Write a function that, given any positive integer input, returns the number of steps needed to get to the closest Fibonacci number, 
#where each step is either adding or subtracting 1 (i.e. x+1 or x-1).
#E.g. If x = 15, the function should return a value of 2 (since 15 - 1 - 1 = 13).



def Fibonacci(n): # number of numbers that want to generate
    fibonacci_list=[0]*n
    fibonacci_list[0]=0
    fibonacci_list[1]=1
    
    if n<2:
        print('input is larger than 2')
    for i in range(2,n):
        fibonacci_list[i]=fibonacci_list[i-1]+fibonacci_list[i-2]
    return fibonacci_list,fibonacci_list[-1]


def step_finding_Fibonacci(integer_input):
    n=2
    while True:
        n+=1
        if integer_input<=Fibonacci(n+1)[1] and integer_input>=Fibonacci(n)[1]: 
            break
    minimum_step=min(abs(Fibonacci(n+1)[1]-integer_input),abs(integer_input-Fibonacci(n)[1]))
    return minimum_step,
    #return n,Fibonacci(n)[1]


step_finding_Fibonacci(30)

#Fibonacci(10)

